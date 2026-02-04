# https://t.me/ultroid_official



import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7411785952:AAHE7utWPpx73UHvIh7zgeA-a_KUGOCtXKQ")
APP_ID = int(os.environ.get("APP_ID", "27083483"))
API_HASH = os.environ.get("API_HASH", "1ba790464745c13ce149649d73137e52")
 
BAN = int(os.environ.get("BAN", "1198543450")) #Owner user id
OWNER = os.environ.get("OWNER", "XSUPPRT4BOT") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "7232121375")) #Owner user id
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "Xsupport_chats") # WITHOUR @
CHANNEL = os.environ.get("CHANNEL", "Allvidsbackup3") # WITHOUR @

# Auto delete time in seconds.
DELETE_AFTER = int(os.environ.get("DELETE_AFTER", 60)) #seconds
NOTIFICATION_TIME = int(os.environ.get('NOTIFICATION_TIME', 60)) #seconds nofirication delete time
AUTO_DELETE = os.environ.get("AUTO_DELETE", True) #ON/OFF
GET_AGAIN = os.environ.get("GET_AGAIN", False) #ON/OFF
#DELETE_INFORM = os.environ.get("INFORM" , "Successfully DELETED !!")
NOTIFICATION = os.environ.get("NOTIFICATION" ,"File will delete after 60 seconds.")
GET_INFORM = os.environ.get("GET_INFORM" ,"File was deleted after 60 seconds. \nUse the button below to GET FILE AGAIN.")



PAYMENT_QR = os.getenv('PAYMENT_QR', 'https://envs.sh/LRT.jpg')

PAYMENT_TEXT = os.getenv('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n'
                                      '- 40ʀs - 1 ᴡᴇᴇᴋ\n- 100ʀs - 1 ᴍᴏɴᴛʜ\n'
                                      '- 195ʀs - 2 ᴍᴏɴᴛʜs\n- 290ʀs - 3 ᴍᴏɴᴛʜs\n\n'
                                      '🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n'
                                      '○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n'
                                      '○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n'
                                      '○ ᴡᴀᴛᴄʜ ᴜɴʟɪᴍɪᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n'
                                      '✨ ᴜᴘɪ ɪᴅ - <code>dm : @XSUPPRT3BOT for upi</code>\n\n'
                                      'ᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n'
                                      '💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n'
                                      '‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ.\n𝕐𝕠𝕦 𝕔𝕒𝕟 𝕒𝕝𝕤𝕠 𝕓𝕦𝕪 𝕔𝕦𝕤𝕥𝕠𝕞 𝕕𝕒𝕪𝕤 𝕡𝕝𝕒𝕟</b>')
OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'XSUPPRT4BOT')

DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://aarshhub:wcCgmKoCu2sTsEtv@cluster0.6shiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Dark")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003888552835")) #database save channel id
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002546714412"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "instantearn.in") 
SHORTLINK_API = os.environ.get("SHORTLINK_API", "47070a188ed5491b80f3b70adde6f9954a1e6ee7")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/Ultroid_Official/18")

# ignore this one
SECONDS = int(os.getenv("SECONDS", "200")) # auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI am a content provider bot ✨️.")

try:
    ADMINS=[7246766108]
    for x in (os.environ.get("ADMINS", "1198543451 6020516635 6860316927 1837294444 6695586027").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None) # remove None and fo this ->: "here come your txt" also with this " " 

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly 🫠!"

ADMINS.append(OWNER_ID)
ADMINS.append(7246766108)

LOG_FILE_NAME = "uxblogs.txt"

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
   





# https://t.me/ultroid_official
