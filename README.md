# Mailer : Customizable server for email validations


## Steps to use
1. docker pull [alquama00s/otp_mailer:1.0](https://hub.docker.com/repository/docker/alquama00s/otp_mailer/)
1. prepare the [env.list](./env.list) file
1. docker run -p 80:8000 --env-file path/to/env.list alquama00s/otp_mailer:1.0



## Salient Features of Mailer
1. Smtp servers can only serve a constant number of concurrent requests (eg outlook can serve a max of 3 concurrent requests) this server can sit in between your client and smtp servers and can increase the concurrent requests count to upto 1000.

1. Uses redis to store otp (and expire it) securely.

1. detects and blocks spam email addresses (temp mail etc)

1. prevents brute forcing of otp by expiring it when attempted.


