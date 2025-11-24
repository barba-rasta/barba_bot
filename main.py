from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import handlers
import time


PREFIX = "!/."


OWNER = ["796121550"]

OWNER_NAME = "Jorgebarba"

CHANNEL = "https://t.me/Jorgebarba"

GROUP = "https://t.me/termuxcomunidad"

def ok(mm):
  mg = str(mm)
  paid = open("paid.txt").read().splitlines()
  if mg in OWNER:
    user = "Dueño"
    return user
  elif mg in paid:
    user = "Pagado"
    return user
  elif mg not in paid:
    user = "Gratis"
    return user
  else:
    user = "Gratis"
    return user

from loader import dp


@dp.message_handler(commands=['start', 'help'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):
  kk = await message.reply("<b> Hello, I'm cc checker  Bot made by *Jorgebarba*</b>")
  time.sleep(2)
  seconds = time.time()
  local_time = time.ctime(seconds)
  await kk.edit_text(
        f"""<b> Hello  @{message.from_user.username} \Welcome to cc Checker bot  : {local_time} \To see all the commands send /cmds \n By the way your UserID is <code> {message.from_user.id} </code>\n Bot by: </b> <a href='https://t.me/Jorgebarba'><b>JORGE BARBA</b></a>""",
    disable_web_page_preview=True)



if __name__ == '__main__':

  executor.start_polling(dp, skip_updates=True)
