import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://github.com/jarvis210904/J.A.R.V.I.S-Userbot/blob/master/jarvis.jpg?raw=true"
pm_caption = "**ᴊᴀʀᴠɪꜱ ɪꜱ ᴏɴʟɪɴᴇ**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/jarvissupportofficial)\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/joinchat/R5-ZBEdh9Uzix53RWtmHiA)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                 : [ᴍɪᴛ ʟɪᴄᴇɴꜱᴇ](https://github.com/jarvis210904/J.A.R.V.I.S-Userbot/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [𝙅𝘼𝙍𝙑𝙄𝙎](GitHub.com/jarvis210904)\n"

pm_caption += " [┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/jarvissupportofficial)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
