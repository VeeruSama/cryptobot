
from telethon import events,Button
import asyncio
from telethon import TelegramClient


Message="Hello There"
JobLink=""
api_id = 8191249
api_hash = '10bd3ac4432d28930afcca6276fc10bd'
Bot_token = '2050705893:AAHGd-AfBJVyfYqAu3LaAf9Fb6Dlpl9EiMs'
client2=TelegramClient('bot',api_id,api_hash).start(bot_token=Bot_token)

def posttotele(msg):
        global Message
        Message=msg
        loop=asyncio.get_event_loop()
        task=loop.create_task(sedner())
        loop.run_until_complete(task)

async def sedner():
        chat=await client2.get_entity("t.me/freshers_jobs_latest")
        await client2.send_message(chat,Message)



