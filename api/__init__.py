from redis_server import redis
from sender import sender
redis_client=redis.Redis()
email_sender=sender.sender(concurrent_connections=3)
email_sender.startSender()
