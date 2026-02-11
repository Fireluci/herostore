import os
import logging
from logging.handlers import RotatingFileHandler

# Multi token support
BOT_TOKEN1 = os.environ.get("BOT_TOKEN1", "")
BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", "")
BOT_TOKEN3 = os.environ.get("BOT_TOKEN3", "")

APP_ID = int(os.environ.get("APP_ID", "1736204"))
API_HASH = os.environ.get("API_HASH", "890d40e0f91a4de32dec2965444b2cbe")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002347173260"))
OWNER_ID = int(os.environ.get("OWNER_ID", "1058015838"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://herostore:herostore@herostore.ywtvule.mongodb.net/?appName=herostore")
DB_NAME = os.environ.get("DATABASE_NAME", "herostore")

SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "easysky.in")
SHORTLINK_API = os.environ.get('SHORTLINK_API', "640eb2125f39b0e70aa9f1baee312655c8f676cd")

FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL")
FORCE_SUB_CHANNEL = int(FORCE_SUB_CHANNEL) if FORCE_SUB_CHANNEL else None

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1058015838").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1058015838)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
