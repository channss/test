FROM python:3.11-slim-buster

WORKDIR /app
COPY test.sh /app
RUN apt-get update ; apt-get upgrade -y \
    && apt-get install curl -y \
    && apt-get install vim -y

ENTRYPOINT ["/bin/sh"]
