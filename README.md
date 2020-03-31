# BOT Telegram [python]

PremiumStateBot is python powered Telegram Bot to connect to a server and execute some check on it

### Set the following environment variable in the Dockerfile

ENV BOT_KEY="TELEGRAM BOT TOKEN"
 
ENV TELNET_PORT="PORT TO CHECK"
 
ENV ADDRESS="IP ADDRESS OR HOSTNAME"
 
ENV USERNAME="USERNAME"

ENV PASSWORD="PASSWORD"
 
ENV UI_PORT="UI PORT of the web service"

### Deploy the Bot in Heroku

This is the deployment procedure with Docker container

Create a personal account in Heroku.com

Download Heroku CLI [here](https://devcenter.heroku.com/articles/heroku-cli)

Login
```sh
heroku container:login
```
Build and push an image
```sh
heroku container:push --app <HEROKU_APP_NAME> web
```
Create a new release
```sh
heroku container:release --app <HEROKU_APP_NAME> web
```
Watch logs
```sh
heroku logs --tail --app <HEROKU_APP_NAME>
```

it could be completly free


### Note
These files are useless to deply by docker container:
 - Procfile 
 - requirements.txt 
they are used by Heroku if you want deploy only the Python script
