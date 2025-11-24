from aiogram import *
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from main import ok,OWNER,OWNER_NAME,CHANNEL,GROUP
from loader import dp
PREFIX = "!/."

#===========================================================================handler ========================================================================


@dp.callback_query_handler(text=["free", "paid", "buy", "close", "other", "back", "hide", "other back"])
async def process_cart(call: types.CallbackQuery):
  if call.data == "free":
    button1 = InlineKeyboardButton(text="💲free gates💲", callback_data="paid")
    button3 = InlineKeyboardButton(text="🔙", callback_data="back")
    button4 = InlineKeyboardButton(text="🔚", callback_data="close")

    keyboard_inline = InlineKeyboardMarkup().add(button1).add(button3, button4)

    await call.message.edit_text("""
<b>
➣ 3D Lookup : OFF

➣ Stripe Auth V4 : /chk""",
                                 reply_markup=keyboard_inline,
                                 disable_web_page_preview=True)



 


  elif call.data == "paid":

    button1 = InlineKeyboardButton(text="💱Paid gates💱", callback_data="free")
    button3 = InlineKeyboardButton(text="🔙", callback_data="back")
    button4 = InlineKeyboardButton(text="🔚", callback_data="close")
    keyboard_inline = InlineKeyboardMarkup().add(button1).add(button3, button4)

    await call.message.edit_text("""<b>
➣ Braintree [Non 3D] : OFF

➣ Usaepay : OFF

➣ BluePay [AVS] : OFF

➣ PayEzzy : OFF

➣ PayFlow : OFF

➣ Recurly : OFF

➣ Stripe Mass Check : OFF

➣ Stripe Charge 1€ : OFF

➣ Stripe Charge 1$ : OFF

➣ Stripe Charge 20$ : OFF

➣ Stripe Charge 0.5$ + Refund : OFF

➣ Stripe Charge 1$ + Refund : OFF

➣ Stripe Charge 5$ + Refund : OFF

➣ Stripe Charge 10$ + Refund : OFF

➣ Stripe Charge 300$ : OFF </b>""",reply_markup=keyboard_inline, disable_web_page_preview=True)

  elif call.data == "buy":
    button1 = InlineKeyboardButton(text="🔚", callback_data="hide")
    button2 = InlineKeyboardButton(text="🔙", callback_data="buy")
    keyboard_inline = InlineKeyboardMarkup().add(button2).add(button1)

    text = f"""
contact @I_M_R_A_S
"""

    await call.message.edit_text(text,reply_markup=keyboard_inline)
  elif call.data == "close":
    try:
      return await call.message.delete()
    except:
       await call.message.edit_text("hidden")
  elif call.data == "back":
    button1 = InlineKeyboardButton(text="💱Paid gates💱", callback_data="free")
    button2 = InlineKeyboardButton(text="💲Free gates💲", callback_data="paid")
    button3 = InlineKeyboardButton(text="🔙", callback_data="other back")
    button4 = InlineKeyboardButton(text="🔚", callback_data="close")
    keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(
      button3, button4)

    await call.message.edit_text(f"""
    <b>
Hello, it seems to me that you are interested in my commands, you can explore by pressing any of the buttons
<b>User type = {call.message.reply_to_message.from_user.full_name}</b> ({ok(call.message.reply_to_message.from_user.id)})
Bot made by: <a href='{CHANNEL}'><b>{OWNER}</b>  </a> </b>""",reply_markup=keyboard_inline,disable_web_page_preview=True)


  elif call.data == "other":


    button2 = InlineKeyboardButton(text="🔙", callback_data="other back")
    button3 = InlineKeyboardButton(text="🔚", callback_data="close")
    keyboard_inline = InlineKeyboardMarkup().add(button2, button3)

    await call.message.edit_text(f"""
<b>
🔥 /sk sk_live_xxx to check sk keys (with balance)

🔥 /bin xxxxxx  to check bin 

🔥 /src cc scraper

🔥 /fake fake address gen

🔥 /gen cc gen
</b>
Bot made by: <a href='{CHANNEL}'><b>{OWNER}</b>  </a> """,reply_markup=keyboard_inline,disable_web_page_preview=True)

  elif call.data == "hide":
    try:
      return await call.message.delete()
    except:
       await call.message.edit_text("hidden")


  elif call.data == "other back":
    button1 = InlineKeyboardButton(text="💳 Checker Gates 💳",callback_data="back")
    button2 = InlineKeyboardButton(text="🔍Tools 🔍",callback_data="other")
    button3 = InlineKeyboardButton(text="🔑Get-access🔑", callback_data="buy")
    button4 = InlineKeyboardButton(text="🔚", callback_data="close")
    
    keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4)

    await call.message.edit_text(f"""
      <b>
Hello, it seems to me that you are interested in my commands, you can explore by pressing any of the buttons
<b>User type = {call.message.reply_to_message.from_user.full_name}</b> ({ok(call.message.reply_to_message.from_user.id)})
Bot made by: <a href='{CHANNEL}'><b>{OWNER}</b>  </a> </b>""",
                                 reply_markup=keyboard_inline,
                                 disable_web_page_preview=True)



#=======================================================commands=======================================================================


#=======================================================commands=======================================================================


@dp.message_handler(commands=['cmd', 'cmds', 'command', 'commands'],
                    commands_prefix=PREFIX)
async def process_cart(message: types.Message):
  button1 = InlineKeyboardButton(text="💳 Checker Gates 💳",callback_data="back")
  button2 = InlineKeyboardButton(text="🔍Tools🔍",callback_data="other")
  button3 = InlineKeyboardButton(text="🔑Get-access🔑", callback_data="buy")
  button4 = InlineKeyboardButton(text="🔚", callback_data="close")
  
  keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4)

  await message.reply(f"""
<b>
Hello, it seems to me that you are interested in my commands, you can explore by pressing any of the buttons
<b>User type = {message.from_user.first_name}</b> ({ok(message.from_user.id)}) 
Bot made by: <a href='{CHANNEL}'>{OWNER_NAME}</a> </b>""",
                      reply_markup=keyboard_inline,
                      disable_web_page_preview=True)





