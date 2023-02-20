import redis
from datetime import timedelta,datetime
from time import time
from threading import Event,current_thread,active_count
import random
import string
from constants.variables import REDIS_SERVER,REDIS_PORT,OTP_TIMEOUT,WA_COUNT
class Redis:
    __list_not_empty_event=Event()
    __client = redis.Redis(host=REDIS_SERVER, port=REDIS_PORT, db=0)
    __code_expiration=timedelta(seconds=OTP_TIMEOUT)
    
    def requestQueueLength(self)->int:
      return self.__client.llen("requests")

    def __otpGenerator(self)->str:
      return ''.join(random.choices(string.digits,k=6))
    
    def setCode(self,email:str)->str:
      if(self.__client.exists(f"{email}:code")==1):
        return self.__client.get(f"{email}:code").decode()
      code=self.__otpGenerator()
      self.__client.set(f"{email}:code",code,self.__code_expiration)
      self.__client.set(f"{email}:wa",0,self.__code_expiration)
      return code

    def __expireCode(self,email:str):
      self.__client.delete(f"{email}:code")
      self.__client.delete(f"{email}:wa")

    def __registerWrongAttempt(self,email:str):
      wa=self.__client.incr(f"{email}:wa")
      if(wa>=WA_COUNT):
        self.__expireCode(email)
        

    def checkCode(self,email:str,code:str)->str:
      if(self.__client.exists(f"{email}:code")==1):
        if(self.__client.get(f"{email}:code").decode()==code):
          self.__expireCode(email)
          return "OK"
        else:
          self.__registerWrongAttempt(email)
          return "wrong code"
      return "not found";

    def __setTimestamp(self,email)->float:
      ts=time()
      self.__client.set(f"{email}:ts",ts)
      return ts

    def removeTimeStamp(self,email):
      ts=float(self.__client.get(f"{email}:ts").decode())
      self.__client.delete(f"{email}:ts")
      return ts

    def publishRequest(self,email:str)->str:
      if(self.__client.exists(f"{email}:ts")==1):
        ts= self.__setTimestamp(email)
        return str(datetime.fromtimestamp(ts))
      ts= self.__setTimestamp(email)
      self.__client.lpush("requests",email)
      # print(f"{current_thread().ident} {active_count()} setting")
      self.__list_not_empty_event.set()
      return str(datetime.fromtimestamp(ts))

    def getRequest(self)->str|None:
      if(self.__client.llen("requests")==0):
        # print(f"{current_thread().ident} {active_count()} request waiting")
        self.__list_not_empty_event.clear()
        self.__list_not_empty_event.wait()
        # print("after wait")
      # print(f"{current_thread().ident} {active_count()} redis->giving request")
      return self.__client.rpop("requests").decode()
      

      

