import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23748681"))
    API_HASH = os.environ.get("API_HASH", "8ac344c214fbc889c837e9eba866751d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5861787158:AAEhhPB0pK0gN4aIiyIgOfNf7T2DIZZ8V-M")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "UNK_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "UNK_SUPPORT") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "UNK_NETWORK") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5979745395")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
