
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from main import dp
from main import ok,OWNER,OWNER_NAME,CHANNEL,GROUP

import requests
from aiogram import  types
PREFIX = "!/."


@dp.message_handler(commands=['bin'], commands_prefix=PREFIX)
async def main(message: types.Message):
  nn = await message.reply("<b>  wait i am checking y our card </b>")
  user = ok(message.from_user.id)
  cc = message.text[len('/bin '):]
  splitter = cc.split('|')
  BIN = splitter[0]
  BIN = cc[:6]
  if len(BIN) < 6:
    return await nn.edit_text('Send bin not ass')
  paid = open("black.txt").read().splitlines()

  if BIN in paid:
    return await nn.edit_text(f''' 
{BIN} <b> is blacklisted </b>
      ''')

  try:
    rem = requests.get(f"https://lookup.binlist.net/{BIN}").json()
    INFO = f'''
<b>Valid Bin</b> ✅

<b> ————Bank Details———— </b>
Bin data -»<b>{rem["scheme"]}</b>-<b>{rem["type"]}</b>-<b>{rem["brand"]}</b>
bank data -»<b>{rem["bank"]["name"]}</b>
Country -»<b>{rem["country"]["name"]} {rem["country"]["emoji"]}</b>


Checked by -» <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{ok(message.from_user.id)}]
  '''

  except:
    INFO = f'''
<b> Invalid Bin </b> 

  '''


  
  await nn.edit_text(INFO)




@dp.message_handler(
  commands=['info', 'id', 'me'], commands_prefix=PREFIX
)  #------------------------------------------------------info-------------------------------------
async def delg(message: types.Message):

  if message.reply_to_message:
    user_id = message.reply_to_message.from_user.id
    is_bot = message.reply_to_message.from_user.is_bot
    username = message.reply_to_message.from_user.username
    first = message.reply_to_message.from_user.first_name

  else:
    user_id = message.from_user.id
    is_bot = message.from_user.is_bot
    username = message.from_user.username
    first = message.from_user.first_name

  await message.reply(f'''
 
<b>USER INFO</b>

<b>👱 NAME:</b><a href="tg://user?id={user_id}">{first}</a>

<b>🆔 ID:</b> <code>{user_id}</code>
<b>🌐 Username:</b> @{username}
<b>👀 User = </b> [{ok(user_id)}]
<b>🤖 IS bot = </b> {is_bot}
''')
