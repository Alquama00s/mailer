from . import send

from redis_server import redis
from time import sleep
class Email:
  redis_client=redis.Redis()
  
  def sendEmail(self,to:str):
    otp=self.redis_client.setCode(to)
    # print(otp)
    sleep(20)
    # send.send_mail(client='dart',to='alquamasalim000@gmail.com',otp=otp)
    print(otp)
    # print("set")



