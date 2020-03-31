
FROM python:3.7

#RUN pip install python-telegram-bot
RUN pip install telepot
RUN apt update
RUN apt install -y nmap 
#RUN pip install pexpect --upgrade

ENV BOT_KEY="TELEGRAM BOT TOKEN"
ENV TELNET_PORT="PORT TO CHECK"
ENV ADDRESS="IP ADDRESS OR HOSTNAME"
ENV USERNAME="USERNAME"
ENV PASSWORD="PASSWORD"
ENV UI_PORT="UI PORT of the web service"

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python /app/app.py
