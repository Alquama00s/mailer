import redis
from datetime import timedelta,datetime
from time import time
from threading import Event,current_thread,active_count
class Redis:
    __list_not_empty_event=Event()
    __client = redis.Redis(host='localhost', port=6379, db=0)
    __code_expiration=timedelta(minutes=1)
    
    def requestQueueLength(self)->int:
      return self.__client.llen("requests")
    
    def setCode(self,email:str,code:str):
      self.__client.set(email,code,self.__code_expiration)

    def checkCode(self,email:str,code:str)->str:
      if(self.__client.exists(email)==1):
        if(self.__client.get(email).decode()==code):
          return "OK"
        else:
          return "wrong code"
      return "code expired";

    def publishRequest(self,email:str)->str:
      ts=time()
      self.__client.lpush("requests",f"{email}:{ts}")
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
      

      

