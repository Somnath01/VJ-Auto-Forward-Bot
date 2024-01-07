from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "ce968070d72fe013582d41e4a1e7bee4")
      API_ID = int(getenv("API_ID", "22636431"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "mongodb+srv://shizuroy1998:6ZR2SMmIS5tlqJQw@cluster0.i5hwgxd.mongodb.net/?retryWrites=true&w=majority")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001795733255:-1001999990315").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
