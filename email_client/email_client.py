from . import send
import random
import string
from redis_server import redis
from time import sleep
class Email:
  redis_client=redis.Redis()

  def __otpGenerator(self)->str:
    return ''.join(random.choices(string.digits,k=6))
  
  
  def sendEmail(self,to:str):
    otp=self.__otpGenerator()
    # print(otp)
    sleep(20)
    # send.send_mail(client='dart',to='alquamasalim000@gmail.com',otp=otp)
    self.redis_client.setCode(to,otp)
    # print("set")



