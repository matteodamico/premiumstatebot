import telepot
import os

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'text':
          name = msg["from"]["first_name"]
          txt = msg['text']
          bot.sendMessage(chat_id, 'ciao %s, sono un bot molto stupido!'%name)
          bot.sendMessage(chat_id, 'ho ricevuto questo: %s'%txt)

TOKEN = os.environ['BOTKEY']

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')

import time
while 1:
    time.sleep(10)
