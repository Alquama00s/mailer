from redis_server import redis
from sender import sender
from constants.variables import MAX_CONCURRENCY
redis_client=redis.Redis()
email_sender=sender.sender(concurrent_connections=MAX_CONCURRENCY)
email_sender.startSender()
