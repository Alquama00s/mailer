from redis_server import redis
import threading
from time import time
from email_client import email_client
class sender:
  discard_count=0;
  send_event=threading.Event()
  current_concurrency=0
  def __init__(self,concurrent_connections:int) -> None:
    self.redis=redis.Redis()
    self.concurrent_connections=concurrent_connections
    self.email_client=email_client.Email()
    

  def getMaxConcurrency(self)->int:
    return self.concurrent_connections

  def startSender(self):
    self.t=threading.Thread(target=self.__startSender)
    self.t.start()


  def __startSender(self):
    while(True):
      # print(f"{self.current_concurrency} here")
      if(self.current_concurrency==self.concurrent_connections):
        # print("waiting")
        self.send_event.clear()
        self.send_event.wait()
      # print(f"{threading.current_thread().ident} trying to fetch request")
      request=self.redis.getRequest()
      # print(f"got req {request}")
      ts=self.redis.removeTimeStamp(request)
      if(time()-ts<=300):
        self.discard_count=0
        t=threading.Thread(target=self.sendCode,args=(request,))
        self.current_concurrency+=1  
        t.start()
      else:
        self.discard_count+=1
      


  def sendCode(self,email:str):
    self.email_client.sendEmail(email)
    self.current_concurrency-=1
    self.send_event.set()  
