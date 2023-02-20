import os

# mailer related
MAIL_ID=os.environ["MAIL_ID"]
MAIL_PASSWORD=os.environ["MAIL_PASSWORD"]
SMTP_PORT=int(os.environ["SMTP_PORT"])
SMTP_HOST=os.environ["SMTP_HOST"]
APPNAME=os.environ["APPNAME"]
MAX_CONCURRENCY=int(os.environ["MAX_CONCURRENCY"])
OTP_TIMEOUT=int(os.environ["OTP_TIMEOUT"])
WA_COUNT=int(os.environ["WA_COUNT"])



# redis related
REDIS_SERVER=os.environ["REDIS_SERVER"]
REDIS_PORT=int(os.environ["REDIS_PORT"])
