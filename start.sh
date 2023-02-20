

list=(
"MAIL_ID"
"MAIL_PASSWORD"
"SMTP_PORT"
"SMTP_HOST"
"APPNAME"
"MAX_CONCURRENCY"
"OTP_TIMEOUT"
"WA_COUNT"
"REDIS_SERVER"
"REDIS_PORT"
"SERVER_MODE"
"SERVER_SECRET_KEY"
)

for i in "${list[@]}"
do
if [[ -z "${!i}" ]]; then
 echo "$i is undefined"
 exit 1
fi
done

redis-server &
gunicorn -c configs/gunicorn/dev.py