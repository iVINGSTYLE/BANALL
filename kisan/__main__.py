from pyrogram import idle
from .config import Config
from . import bot
bot.start()
idle()
bot.stop()
