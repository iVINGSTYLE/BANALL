import os
from os import getenv

class Config:
    BOT_TOKEN = getenv("BOT_TOKEN", None)
    STRING_SESSION = getenv("STRING_SESSION", None)
    API_HASH= getenv('API_HASH')
    API_ID=int(getenv('API_ID'))
        
    if not API_HASH:
        raise ValueError("API_HASH not set")

    if not API_ID:
        raise ValueError("API_ID not set")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not set")
