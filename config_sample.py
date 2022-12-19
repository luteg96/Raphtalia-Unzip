import os

class Config(object):
    # Mandotory
    APP_ID = 
    API_HASH = ""
    BOT_TOKEN = ""
    LOGS_CHANNEL = ""
    BOT_OWNER = ""
    MONGODB_URL = ""
    GOFILE_TOKEN = ""
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Raphtalia"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
