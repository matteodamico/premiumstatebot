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

def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
          name = msg["from"]["first_name"]
          txt = msg['text']
          bot.sendMessage(chat_id, 'ciao %s! Che vuoi fare?'%name)
          if txt == 'Checkport':
            bot.sendMessage(chat_id, 'eseguo il comando: %s'%txt)
            checkportresult=subprocess.check_output("nmap -Pn -p "+ TELNET_PORT +" "+ ADDRESS + " | awk '{print $2}' | awk 'NR==6'",shell=True)
            bot.sendMessage(chat_id, 'stato porta: %s'%checkportresult)
          if txt == 'Standby':
            bot.sendMessage(chat_id, 'eseguo il comando: %s'%txt)
            stanbyresult=subprocess.check_output("wget -O /dev/null -q http://" + USERNAME +":"+ PASSWORD +"@"+ ADDRESS +":"+ UI_PORT +"/web/powerstate?newstate=0", shell=True)
            bot.sendMessage(chat_id, 'comando esguito con successo: %s'%stanbyresult)
          if txt == 'Screenshot':
            bot.sendMessage(chat_id, 'eseguo il comando: %s'%txt)
            image=subprocess.check_output("wget -O screen.jpeg -q http://" + USERNAME +":"+ PASSWORD +"@"+ ADDRESS +":"+ UI_PORT +"/grab", shell=True)
            bot.sendPhoto(chat_id, photo=open('screen.jpeg', 'rb'))
          if txt == 'Wake':
            bot.sendMessage(chat_id, 'eseguo il comando: %s'%txt)
            wakeresult=subprocess.check_output("wget -O /dev/null -q http://" + USERNAME +":"+ PASSWORD +"@"+ ADDRESS +":"+ UI_PORT +"/web/remotecontrol?command=116", shell=True)
            bot.sendMessage(chat_id, 'comando esguito con successo: %s'%wakeresult)
#         if txt == 'Restart':
#            bot.sendMessage(chat_id, 'eseguo il comando: %s'%txt)
#            restartresult=subprocess.check_output("wget -O /dev/null -q http://" + USERNAME +":"+ PASSWORD +"@"+ ADDRESS +":"+ UI_PORT +"/web/remotecontrol?command=116", shell=True);
#            bot.sendMessage(chat_id, 'comando esguito con successo: %s'%restartresult)

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
