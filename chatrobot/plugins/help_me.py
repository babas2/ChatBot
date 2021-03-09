
#    Copyright (C) DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from chatrobot.plugins.sql.users_sql import add_me_in_db, his_userid
from chatrobot.plugins.sql.checkuser_sql import add_usersid_in_db, already_added, get_all_users
from telethon import custom, events, Button
import re
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

@chatbot_cmd("start", is_args=False)
async def sedlyfsir(event):
    starkbot = await chatbot.get_me()
    bot_id = starkbot.first_name
    bot_username = starkbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    oknoob = Config.OWNER_ID
    oksir = Config.CUSTOM_START
    if Config.CUSTOM_START is None:
        text_me = (f"**Salam {firstname} , mən {bot_username}.** \n"
               f"`Mən səninlə danışmaq üçün botam.` [Sahibim](https://t.me/c9ala) \n"
               f"**Şikayət və təkliflər üçün sahibimə yazın.** \n"
               f"**Təşəkkürlər.**")
    else:
        text_me = f"{oksir}"
    formaster = "Salam. Sizə necə kömək edə bilərəm?"
    if event.sender_id == Config.OWNER_ID:
        ok = await chatbot.send_message(event.chat_id, message=formaster, buttons = [
             [custom.Button.inline("Commands For Owner.", data="cmds")],
             [custom.Button.inline("Close 🔐", data="close ")],
              ]
             )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
            await chatbot.send_message(Config.DUMB_CHAT, f"YENİ İSDİFADEÇİ ! \nUser ID : `{event.chat_id}`")
        await chatbot.send_message(event.chat_id, text_me)
    

    
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mewant")))
async def help(event):
    if event.query.user_id is not Config.OWNER_ID:
        await event.edit(
            "You Can Deploy Your Own ChatBot By Watching Video Down There. \nThank You For Contacting Me.",
            buttons=[
                [Button.url("Rəsmi Kanal 📺", "t.me/c0alaa")],
                [Button.url("Kömək ❓", "t.me/c9ala")],
            ],
        )
        
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def help(event):
    await event.delete()
              
              
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"cmds")))
async def help(event):
    msg = (f"<b><u> Commands </b></u> \n<code>➤ /start - Starts Bot \n➤ /block - cavab verilen isdifadəçini bloklamaq \n➤ /unblock - İsdifadeçini blokdsn çıxarmaq \n➤ /alive - mən yaşıyıram? 🤧 \n➤ /broadcast - Broadcasts A Message \n➤ /stats - bot statistikası </code>")
    await event.edit(msg, parse_mode="HTML")
