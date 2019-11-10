from telethon import events
from uniborg.util import admin_cmd

@borg.on(admin_cmd("repo"))
async def handler(event):
    await event.edit("[Click here](https://github.com/Amazers03/uniborg1) to open this lit repo!")
