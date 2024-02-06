
from kisan import app
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@app.on_message(
filters.command("banall") 
& filters.group
)
async def banall_command(client, message: Message):
  print("getting memebers from {}".format(message.chat.id))
  async for i in app.get_chat_members(message.chat.id):
      try:
          await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
          print("kicked {} from {}".format(i.user.id, message.chat.id))
      except Exception as e:
          print("failed to kicked {} from {}".format(i.user.id,e))           
  print("process completed")
  return await message.reply_text(f"⚠️ Banned All Members")
