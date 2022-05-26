import aiohttp
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import os
from config import *
import logging 
import logging.config
                            
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)             

FORCE_SUB = os.environ.get("FORCE_SUB", None)           

app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

print("[INFO]: STARTING BOT...")
app.start()

print("[INFO]: STARTING AIOHTTP CLIENT")
session = aiohttp.ClientSession()
