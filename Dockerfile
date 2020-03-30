
FROM python:3.7

#RUN pip install python-telegram-bot
RUN pip install telepot
RUN apt update
RUN apt install -y nmap 
#RUN pip install pexpect --upgrade

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python /app/app.py
