import asyncio
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from kisan import config
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@banbot.on_message(filters.command("banall"))
async def being_devil(_, message: Message):
    if message.chat.type == enums.ChatType.GROUP or message.chat.type == enums.ChatType.SUPERGROUP:
        starter = message.from_user.id
        cid = message.chat.id
        LOGGER.info(f"{starter} started a task in {cid}")
        adminlist = []
        async for admin in banbot.get_chat_members(chat_id=cid, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            adminlist.append(admin)
        global adminlist2
        adminlist2 = adminlist.copy()
        for admin2 in adminlist:
            userinfo = adminlist[admin2]
            if userinfo.id != starter:
                adminlist.remove(userinfo) # or adminlist.pop(admin2)
            else:
                adminlist.append(starter)
        if starter in adminlist:
            admin3 = adminlist[0]
            if admin3.privileges.can_restrict_members == True:
                botid = Config.BOT_TOKEN.split(":")[0]
                selfuser = await banbot.get_chat_member(chat_id=cid, user_id=botid)
                if selfuser.privileges.can_restrict_members == True:
                    await message.reply("Confirm your action bro\nChoose either :\n• Kick all members except the admins\n• **Ban** all members except the admins\n• Cancel your task", reply_markup=Buttons.CONFIRMATION)
                else:
                    LOGGER.warning("Bot cannot ban members")
                    return message.reply("You need to add me as admin with the following scope : `can_restrict_members`\n__(Turn on \"Ban members\")__")
            else:
                LOGGER.warning("User cannot ban members")
                return message.reply("You are admin, but… You're missing the following scope : `can_restrict_members`\nAsk to a higher admin to give you the ability to ban members")
        else:
            LOGGER.warning("Not admin")
            return message.reply("You aren't admin 😐 Don't mess around with me")
    else:
        LOGGER.warning("Not in group")
        return message.reply("Bruh, do it in a group 😐\nI might be able to do it in channels soon, however I don't see any interest in it. PM **@EDM115** for requesting that feature")
