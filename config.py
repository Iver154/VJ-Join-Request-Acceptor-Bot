from os import environ

API_ID = int(environ.get("API_ID", "16767636"))
API_HASH = environ.get("API_HASH", "adfd92666a3cce231cf750514a57920d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7730879541:AAHFQ2tXu0HZOjcob34ZQBZNSx-lrlNycBs")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002350549709"))
ADMINS = int(environ.get("ADMINS", "808533633"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://shintobenjaman702:RnNS95pCXK402giB@cluster0.qjz2s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "Cluster00")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
