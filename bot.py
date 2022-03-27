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

START_MSG = "<b>👻 𝗛𝗘𝗟𝗟𝗢 !! {},\n\nI'm <a href=https://t.me/Hithaishi_Auto_Delete_BOT>🍀 𝗔𝗨𝗧𝗢 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 🅓🅔🅛🅔🅣🅔 🄱🄾🅃 🚮</a>\n\n✨ 𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦 : I can Delete messages in a group After Specific TIME  <spoiler>𝗘𝗩𝗘𝗡 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦 𝗢𝗙 𝗢𝗧𝗛𝗘𝗥 𝗕𝗢𝗧𝗦 🤖</spoiler>\n\n\n⚡️ 𝗖𝗥𝗘𝗗𝗜𝗧𝗦 : <a href=https://t.me/Hithaishidesai_605>😎 𝗛𝗜𝗧𝗛𝗔𝗜𝗦𝗛𝗜 𝗗𝗘𝗦𝗔𝗜 😎</a></b>"


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
print("👻 User Alive!")
Bot.start()
print("🤖 Bot Alive!")

idle()

User.stop()
print("👻 User Dead!")
Bot.stop()
print("🤖 Bot Dead!")
