FROM python:3.10.9-alpine3.17

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
RUN apk update
RUN apk upgrade
RUN apk add bash
RUN apk --update add redis 




CMD ["bash","start.sh"]
# CMD [ "python3", "vision_server/manage.py", "runserver", "0.0.0.0:8000"]