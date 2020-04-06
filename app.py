import telepot
import os
import subprocess
#import pxssh
#from pexpect import pxssh

TOKEN = os.environ['BOTKEY']
TELNET_PORT = os.environ['TELNET_PORT']
#SSH_PORT= os.environ['SSH_PORT']
ADDRESS = os.environ['ADDRESS']
USERNAME= os.environ['USERNAME']
PASSWORD= os.environ['PASSWORD']
UI_PORT = os.environ['UI_PORT']

WGET_METHOD="wget -O /dev/null -q "
BASE_URL= "http://" + USERNAME +":"+ PASSWORD +"@"+ ADDRESS +":"+ UI_PORT
SUCCESSFULL_COMMAND_TXT="comando eseguito con successo: %s"

def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
          name = msg["from"]["first_name"]
          txt = msg['text']
          bot.sendMessage(chat_id,'ciao %s! Che vuoi fare?'%name)
          if txt == 'Checkport':
            bot.sendMessage(chat_id,'eseguo il comando: %s'%txt)
            checkportresult=subprocess.check_output("nmap -Pn -p "+ TELNET_PORT +" "+ ADDRESS + " | awk '{print $2}' | awk 'NR==6'",shell=True)
            bot.sendMessage(chat_id, 'stato porta: %s'%checkportresult)
          if txt == 'Standby':
            bot.sendMessage(chat_id,'eseguo il comando: %s'%txt)
            stanbyresult=subprocess.check_output(WGET_METHOD + BASE_URL +"/web/powerstate?newstate=0",shell=True)
            bot.sendMessage(chat_id, SUCCESSFULL_COMMAND_TXT%stanbyresult)
          if txt == 'Screenshot':
            bot.sendMessage(chat_id,'eseguo il comando: %s'%txt)
            image=subprocess.check_output("wget -O screen.jpeg -q "+ BASE_URL +"/grab",shell=True)
            bot.sendPhoto(chat_id, photo=open('screen.jpeg', 'rb'))
          if txt == 'Wake':
            bot.sendMessage(chat_id,'eseguo il comando: %s'%txt)
            wakeresult=subprocess.check_output(WGET_METHOD + BASE_URL +"/web/remotecontrol?command=116",shell=True)
            bot.sendMessage(chat_id, SUCCESSFULL_COMMAND_TXT%wakeresult)
          if txt == 'chan':
            bot.sendMessage(chat_id,'eseguo il comando: %s'%txt)
            skyresult=subprocess.check_output(WGET_METHOD + BASE_URL +"/web/zap?sRef=1:0:19:C2:385:110:EEEE0000:0:0:0:",shell=True)
            bot .sendMessage(chat_id, SUCCESSFULL_COMMAND_TXT%skyresult)
          if txt == 'Riavvia cam':
            bot.sendMessage(chat_id,'eseguo il comando: %s'%txt)
            bluresult=subprocess.check_output(WGET_METHOD + BASE_URL +"/web/remotecontrol?command=401",shell=True)
            okresult=subprocess.check_output(WGET_METHOD + BASE_URL +"/web/remotecontrol?command=352",shell=True)
            bot.sendMessage(chat_id, SUCCESSFULL_COMMAND_TXT%bluresult)
          if txt == 'Riavvia dec':
            bot.sendMessage(chat_id, 'eseguo il comando: %s'%txt)
            restartresult=subprocess.check_output(WGET_METHOD + BASE_URL+ "/web/powerstate?newstate=2",shell=True);
            bot.sendMessage(chat_id, SUCCESSFULL_COMMAND_TXT%restartresult)
#            s = pxssh.pxssh()
#            if not s.login (ADDRESS, USERNAME, PASSWORD, port=SSH_PORT):
#              bot.sendMessage(chat_id,'SSH session failed on login.')
#              print str(s)
#            else:
#              bot.sendMessage(chat_id,'SSH session login successful')
#              s.sendline ('reboot')
#              s.prompt()         # match the prompt
#              print s.before     # print everything before the prompt.
#              s.logout()
#          bot.sendMessage(chat_id, '%s esguito con successo'%txt)
# We can also execute multiple command like this:
# s.sendline ('uptime;df -h')

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')

import time
while 1:
    time.sleep(10)
