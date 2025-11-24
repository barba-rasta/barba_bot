from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import requests
from main import PREFIX , ok
from aiogram import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import Throttled
ANTISPAM = int(60)
import re
import concurrent.futures
from handlers.user.newf import new_func2,checkLuhn



@dp.message_handler(commands=['ssh'], commands_prefix=PREFIX)
async def mas2(message: types.Message):
  proxies = {
"http": "http://gate.proxiware.com:2000",
"https": "http://gate.proxiware.com:2000"
}
  kk = await message.reply('<b>checking  ...</b>')
  ug = message.chat.type
  m = message.from_user.id
  kc = ok(m)
  if "private" in ug:
    if "796121550" in kc or "PAID" in kc:
      pass

    else:
      button3 = InlineKeyboardButton(text="Join",
                                     url="https://t.me/cyberassemble")
      keyboard_inline = InlineKeyboardMarkup().add(button3)
      return await kk.edit_text(
        "<b> 🚫 chats not allowed 🚫\nTo use me for free  Join   </b>",
        reply_markup=keyboard_inline,
        disable_web_page_preview=True)
    pass
  elif "supergroup" in ug or "group" in ug:
    guid = f'{message.chat.id}'

    paid = open("group.txt").read().splitlines()
    if guid in paid:

      try:
        if "OWNER" in kc or "PAID" in kc:
          pass
        else:
          await dp.throttle('chk', rate=ANTISPAM)
      except Throttled:
        keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
        btns = types.InlineKeyboardButton("Take Premium ",
                                          url="https://t.me/cyberassemble")
        button2 = InlineKeyboardButton(text="close", callback_data="close")
        keyboard_markup.row(btns, button2)
        return await kk.edit_text(
          """<b> Sorry Request Bloced Due To Antispam  Try Again After Some Time</b>""",
          reply_markup=keyboard_markup,
          disable_web_page_preview=True)

    else:
      button3 = InlineKeyboardButton(text="Join",
                                     url="https://t.me/cyberassemble")
      keyboard_inline = InlineKeyboardMarkup().add(button3)
      return await kk.edit_text(
        f"<b> 🚫 chats not allowed 🚫\nTo use me for free  Join  https://t.me/termuxcomunidad </b>",
        reply_markup=keyboard_inline,
        disable_web_page_preview=True)
  else:
    button3 = InlineKeyboardButton(text="Join",
                                   url="https://t.me/cyberassemble")
    keyboard_inline = InlineKeyboardMarkup().add(button3)
    return await kk.edit_text(
      f"<b> 🚫 chats not allowed 🚫\nTo use me for free  Join  https://t.me/termuxcomunidad</b>",
      reply_markup=keyboard_inline,
      disable_web_page_preview=True)

  await kk.edit_text("Wait gettting valid cards from your input.")
  all_cards = message.text.split('\n')
  keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
  btns = types.InlineKeyboardButton("Take Premium", url="https://t.me/Jorgebarba")
  keyboard_markup.row(btns)

  if len(all_cards) > 11:
    len_cards = len(all_cards)
    if "OWNER" in kc or "PAID" in kc:
      if len(all_cards) > 51:
        await message.answer(f"""found {len_cards}max cards allowed 50 cards """)
        pass
    else:
      await message.answer(f"""<b> found-{len_cards} max cards allowed 10 cards \nTake Premium to check more then 10 </b>""",
        reply_markup=keyboard_markup,
        disable_web_page_preview=True)

  if "OWNER" in kc or "PAID" in kc:
    all_cards = (all_cards[0:50])
  else:
    all_cards = (all_cards[0:10])

  cards = []
  for x in all_cards:
    input = re.findall(r"[0-9]+", x)
    if not input or len(input) < 3:
      continue
    if len(input) == 3:
      cc = input[0]
      if len(input[1]) == 3:
        mes = input[2][:2]
        ano = input[2][2:]
        cvv = input[1]
      else:
        mes = input[1][:2]
        ano = input[1][2:]
        cvv = input[2]
    else:
      cc = input[0]
      if len(input[1]) == 3:
        mes = input[2]
        ano = input[3]
        cvv = input[1]
      else:
        mes = input[1]
        ano = input[2]
        cvv = input[3]
      if len(mes) == 2 and (mes > '12' or mes < '01'):
        ano1 = mes
        mes = ano
        ano = ano1
    if cc and not checkLuhn(cc): continue
    if (cc, mes, ano, cvv):
      cards.append([cc, mes, ano, cvv])
    else:
      continue

  len_cards = len(cards)
  if not len_cards:
    return await kk.edit_text("give me some cards man ."
                              )
  await kk.edit_text(
    "got {} Cards wait ...".format(len_cards))
  text = f"""
Gateway-» <b>Stripe  mass </b>
Total cards : <b>{len_cards}</b>
<b>————Other Details————</b>
Checked by -» <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>[{kc}]
Bot by -» <b> <a href="tg://user?id=796121550"> <b> RAS</b> </a> </b>
Response-»\n
"""

  r = requests.Session()
  for inp in cards:
    with concurrent.futures.ThreadPoolExecutor() as executor:
      future = executor.submit(new_func2, r, inp[0], inp[3], inp[1], inp[2])
      return_value = future.result()
      text += return_value
      await kk.edit_text(text)
  text += f"<i>{len_cards}cards  successfully checked </i>"
  await kk.edit_text(text,disable_web_page_preview=True)


