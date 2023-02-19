# Mailer : Customizable server for email validations

## Salient Features of Mailer
1. Smtp servers can only serve a constant number of concurrent requests (eg outlook can serve a max of 3 concurrent requests) this server can sit in between your client and smtp servers and can increase the concurrent requests count to upto 1000.

1. Uses redis to store otp (and expire it) securely.

1. detects and blocks spam email addresses (temp mail etc)

1. prevents brute forcing of otp by expiring it when attempted.
