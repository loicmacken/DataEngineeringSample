FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --break-system-packages

COPY . .

CMD python3 main.py