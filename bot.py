import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>š» ššššš¢ !! {},\n\nI'm <a href=https://t.me/Hithaishi_Auto_Delete_BOT>š ššØš§š¢ š šš¦š¦ššš ššššš£š š±š¾š š®</a>\n\nāØ šššš§šØš„šš¦ : I can Delete messages in a group After Specific TIME  <spoiler>šš©šš” š šš¦š¦šššš¦ š¢š š¢š§ššš„ šš¢š§š¦ š¤</spoiler>\n\n\nā”ļø šš„šššš§š¦ : <a href=https://t.me/Hithaishidesai_605>š ššš§šššš¦šš ššš¦šš š</a></b>"


User = Client(session_name=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(session_name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
User.start()
print("š» User Alive!")
Bot.start()
print("š¤ Bot Alive!")

idle()

User.stop()
print("š» User Dead!")
Bot.stop()
print("š¤ Bot Dead!")
