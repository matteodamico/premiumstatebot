
FROM python:3.7

#RUN pip install python-telegram-bot
RUN pip install telepot

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python /app/app.py
