from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types.chat import ChatActions
from loader import dp

from aiogram import *
from main import ok,OWNER,OWNER_NAME,CHANNEL,GROUP
PREFIX = "!/."


@dp.message_handler(commands=['ap'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):
  mm = message.from_user.id
  kc = ok(mm)
  if "OWNER" in kc:
    try:
      first = message.reply_to_message.from_user.first_name
      user_id = message.reply_to_message.from_user.id

    except:

      user_id = message.text[len('/ap '):]
      first = user_id

    else:
      button1 = InlineKeyboardButton(text="hide", callback_data="hide")
      keyboard_inline = InlineKeyboardMarkup().add(button1)
      return await message.reply(
        ''' <b>🚫 please provide me uid to promote  \nexample-> /ap xxxxxxxx</b>''',
        reply_markup=keyboard_inline)

    paid = open("paid.txt").read().splitlines()

    if user_id in paid:
      return await message.reply(f''' 
<a href="tg://user?id={user_id}">{first}</a>  <b> is already a Premium </b>
        ''')
    else:
      with open("paid.txt", "a") as f:
        f.write(f"{user_id}\n")

      return await message.reply(
        f'''<b> Congrulations <a href="tg://user?id={user_id}">{first}</a>  Now You Are A member Of Premium Family ✅  \nNow You Access me Without AntiSapam And Use my paid Gates</b>'''
      )


  else:

    button1 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("""🚫 you cannot use this command 🚫""",
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)




@dp.message_handler(commands=['blacklist'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  mm = message.from_user.id
  kc = ok(mm)

  if "OWNER" in kc:

    cc = message.text[len('/blacklist '):]
    BIN = str(cc[:6])
    if len(BIN) < 6:
      return await message.reply(f''' <b>🚫 invalid bin   </b>''')

    paid = open("black.txt").read().splitlines()

    if BIN in paid:
      return await message.reply(f''' 
{BIN} <b> is already a blacklisted </b>
        ''')
    else:
      with open("black.txt", "a") as f:
        f.write(f"{BIN}\n")

      return await message.reply(f'''<b> {BIN} is  blacklisted </b>''')

  elif "PAID" in kc:
    button1 = InlineKeyboardButton(text="hide", callback_data="hide")
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply(f''' 🚫 only OWNER can blacklist  </b>''',
                               reply_markup=keyboard_inline)

  else:

    button1 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("""🚫 you cannot use this command 🚫""",
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)


@dp.message_handler(commands=['admin'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  if message.reply_to_message:

    first = message.reply_to_message.from_user.first_name
  else:

    first = message.from_user.first_name
  m = message.from_user.id
  kc = ok(m)

  if "OWNER" in kc:

    try:

      user_id = str(message.reply_to_message.from_user.id)

    except:
      button1 = InlineKeyboardButton(text="hide", callback_data="hide")
      keyboard_inline = InlineKeyboardMarkup().add(button1)
      return await message.reply(
        ''' <b>🚫 please reply to any message</b>''',
        reply_markup=keyboard_inline)

    paid = OWNER

    if user_id in paid:
      return await message.reply(f''' 
<a href="tg://user?id={user_id}">{first}</a>  <b> is already admin</b>
        ''')
    else:
      OWNER.append(user_id)

      return await message.reply(
        f'''<b>  <a href="tg://user?id={user_id}">{first}</a> is now admin  </b>'''
      )

  elif "PAID" in kc:
    button1 = InlineKeyboardButton(text="hide", callback_data="hide")
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply(
      f''' {first} <b> 🚫 only OWNER can promote</b>''',
      reply_markup=keyboard_inline)

  else:

    button1 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("""🚫 you cannot use this command 🚫""",
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)


@dp.message_handler(commands=['dadmin'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  if message.reply_to_message:

    first = message.reply_to_message.from_user.first_name
  else:

    first = message.from_user.first_name
  m = message.from_user.id
  kc = ok(m)

  if "OWNER" in kc:

    try:

      user_id = str(message.reply_to_message.from_user.id)

    except:
      button1 = InlineKeyboardButton(text="hide", callback_data="hide")
      keyboard_inline = InlineKeyboardMarkup().add(button1)
      return await message.reply(
        ''' <b>🚫 please reply to an owner command </b>''',
        reply_markup=keyboard_inline)

    paid = OWNER
    if user_id =="5234223466":
      return await message.reply(f''' 
<b>🚫 you cannot demote owner </b>
        ''')
    if user_id in paid:
      await message.reply(f''' 
<a href="tg://user?id={user_id}">{first}</a>  <b> is demoted from owner  </b>
        ''')

      OWNER.remove(user_id)
      return
    else:
      return await message.reply(f''' 
<a href="tg://user?id={user_id}">{first}</a>  <b> is Not In OWner List  </b>
        ''')

  elif "PAID" in kc:
    button1 = InlineKeyboardButton(text="hide", callback_data="hide")
    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply(
      f''' {first} <b> 🚫 only OWNER can promote</b>''',
      reply_markup=keyboard_inline)

  else:

    button1 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("""🚫 you cannot use this command 🚫""",
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)




@dp.message_handler(commands=['dp', 'demote'], commands_prefix=PREFIX)
async def igfgnfokc(message: types.Message):

  if message.reply_to_message:

    first = message.reply_to_message.from_user.first_name
  else:

    first = message.from_user.first_name
  m = message.from_user.id
  kc = ok(m)

  if "OWNER" in kc:

    try:

      user_id = str(message.reply_to_message.from_user.id)

      paid = open("paid.txt").read().splitlines()

      if user_id not in paid:
        return await message.reply(f''' 
<a href="tg://user?id={user_id}">{first}</a>  <b> 🚫 is not in Premium list </b>
        ''')
      else:
        await message.reply(
          f''' <b>✅ <a href="tg://user?id={user_id}">{first}</a> To purchase a our bot , contact the owner {OWNER_NAME} </b>'''
        )
        word = f'{message.reply_to_message.from_user.id}'

        with open("paid.txt", "r") as fp:
          lines = fp.readlines()
        with open("paid.txt", "w") as fp:
          for line in lines:
            if line.strip("\n") != word:
              fp.write(line)
              fp.close()
        return



    except:
      return await message.reply(
        ''' <b>🚫  please provide me valid uid to promote  🚫</b>''')

  elif "PAID" in kc:
    return await message.reply(
      f''' {first} <b>🚫 only OWNER can demote  🚫</b>''')

  else:

    button1 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("""you cannot use this command """,
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)


#--------------------------------------------------------data---------------------------------------------------------------------------------


@dp.message_handler(commands=['data'], commands_prefix=PREFIX)
async def infokfhfc(message: types.Message):

  m = message.from_user.id
  kc = ok(m)
  kkc = await message.reply(f'''<b> searching</b>''')
  text = ""
  if "OWNER" in kc:
    PAID = open("paid.txt").readlines()
    running = 0
    for paid in PAID:
      running += 1
      text += f'<a href="tg://user?id={paid}">{paid}</a>'
      await kkc.edit_text(f"{text}✅ Total User={running}")

  elif "PAID" in kc:
    return await message.reply(''' <b> 🚫 only Owner Can See 🚫 </b>''')

  else:

    button4 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button4)
    return await message.reply("""🚫you cannot use this commands 🚫""",
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)


#------------------------------------------------------group promote  --------------=-------------------------------------------------------------------


@dp.message_handler(commands=['addgp'], commands_prefix=PREFIX)
async def infokfc(message: types.Message):

  guid = message.chat.id
  m = message.from_user.id
  kc = ok(m)

  if "OWNER" in kc:
    try:

      guid = f'{message.chat.id}'

      gps = open("group.txt").read().splitlines()

      if guid in gps:
        return await message.reply(
          f'''  {message.chat.full_name}  <b> is already authorised</b>
        ''')
      else:
        with open("group.txt", "a") as f:
          f.write(f"{guid}\n")

        return await message.reply(
          f''' <b> {message.chat.full_name} ✅ is now a  authorised </b>''')

    except:
      return await message.reply(''' <b>🚫 please provide me something  </b>''')

  elif "PAID" in kc:
    return await message.reply(f''' <b> 🚫 only OWNER can promote  </b>''')

  else:

    button1 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("""🚫 you cannot use this command 🚫""",
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)


#------------------------------------------------------demoye  group  --------------=-------------------------------------------------------------------


@dp.message_handler(commands=['delgp'], commands_prefix=PREFIX)
async def igfgnfokc(message: types.Message):
  m = message.from_user.id
  kc = ok(m)

  if "OWNER" in kc:

    try:

      guid = str(message.chat.id)

      gps = open("group.txt").read().splitlines()

      if guid not in gps:
        return await message.reply(
          f''' </a>  <b> 🚫 is not in authorised chats  </b>''')
      else:
        await message.reply(
          f''' <b>✅{message.chat.full_name} is removed from authorised chats contact {OWNER_NAME} </b>''')
        word = f'{message.chat.id}'

        with open("group.txt", "r") as fp:
          lines = fp.readlines()
        with open("group.txt", "w") as fp:
          for line in lines:
            if line.strip("\n") != word:
              fp.write(line)
              fp.close()
              return
            return
          return
        

    except:
      return await message.reply(
        ''' <b>🚫  please provide me uid to promote  🚫</b>''')

  elif "PAID" in kc:
    return await message.reply(f''' <b>🚫 only OWNER can demote  🚫</b>''')

  else:

    button1 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button1)
    return await message.reply("""you cannot use this command """,
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)


#------------------------------------------------------group data --------------=-------------------------------------------------------------------


@dp.message_handler(
  commands=['gdata'], commands_prefix=PREFIX
)  #------------------------------------------------------promote-------------------------------------
async def infokfhfc(message: types.Message):

  m = message.from_user.id
  gg = await message.reply("searching")
  text = ""
  kc = ok(m)

  if "OWNER" in kc:
    gps = open("group.txt").readlines()
    running = 0
    for paid in gps:
      running += 1
      text += f'<a href="tg://user?id={paid}">{running}----</a> <code>{paid}</code>'
      await gg.edit_text(f"{text}✅ Total User={running}")

  elif "PAID" in kc:
    return await message.reply(''' <b> 🚫 only Owner Can See 🚫 </b>''')

  else:

    button4 = InlineKeyboardButton(text="hide", callback_data="hide")

    keyboard_inline = InlineKeyboardMarkup().add(button4)
    return await message.reply("""🚫you cannot use this commands 🚫""",
                               reply_markup=keyboard_inline,
                               disable_web_page_preview=True)


# #------------------------------------------------------group info --------------=-------------------------------------------------------------------
@dp.message_handler(commands=['gp'], commands_prefix=PREFIX)
async def example_func(message: types.Message):
  ug = message.chat.type
  if "supergroup" in ug or "group" in ug:
    guid = f'{message.chat.id}'

    paid = open("group.txt").read().splitlines()
    if guid in paid:
      return await message.reply(f'''<b> ✅ this chat is authorised  </b>''')
    else:
      return await message.reply(f"<b> 🚫 this chat is not authorised  </b>")
  elif ug == "private":
    m = message.from_user.id
    kc = ok(m)
    if "OWNER" in kc or "PAID" in kc:

      return await message.reply(''' 
    god welcome  :)
            ''')

    else:
      return await message.reply(f"<b> 🚫  private chats not allowed </b>")
  else:
    return await message.reply(
      f"<b>  🚫 You Cannot use This Bot IN Private Chat 🚫  </b>")


#======================================================================start====================================================
