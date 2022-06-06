from os import getenv
from dotenv import load_dotenv
import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# API By TechZBots || https://t.me/TechZBots
LOGO_API_URL1 = "tidbl2VtakZ7SbQfYB+llcQMJlba/zopzuLm16IH5x8="

LOGO_API_URL2 = "tidbl2VtakZ7SbQfYB+llcQMJlba/zopzuLm16IH5x8="

#mkn edits😉

DB_URL = os.environ.get("DB_URL", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '900873119').split()]

FORCE_SUB = os.environ.get("FORCE_SUB", "beta_bot_updates")
