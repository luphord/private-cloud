FROM python:3.7-alpine

RUN pip install --no-cache-dir ihatemoney==4.1.5
RUN apk update && apk add openssl

COPY ./run_ihatemoney.sh /bin

EXPOSE 80

ENTRYPOINT [ "run_ihatemoney.sh" ]