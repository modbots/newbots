<p align="center">
<h1><a href="https://telegram.me/AviAnyDLbot">😎 Avi AnyDL Bot</a></h1></p>


---

An Open Source ALL-In-One Telegram RoBot, that can do lot of things.

### Thanks to
• @HexBots


### Installation

#### The Easy Way

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### The Hard Way

```sh
virtualenv -p python3 VENV
. ./VENV/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python bot.py
```

An example `config.py` file could be:

**Not All of the variables are mandatory**

```python3
from sample_config import Config

class Development(Config):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN = ""
  AUTH_USERS = [
      "7351948"
      # is a string for LEGACY purposes
  ]
```

### [@BotFather](https://telegram.dog/BotFather) Commands

```
start - Check if the Bot is Online!
help - How to use this Bot?
me - Check Your Subscription
upgrade - Upgrade your status
deletethumbnail - Delete/Cleared saved Custom Thumbnail
getlink - Get Low Speed Direct Download Link
converttoaudio - Convert Video Files in Telegram Audio
converttovideo - Convert to Streamable Video
rename - (Long Press) and Rename Telegram File
ffmpegrobot - Get Info
trim - (Long Press) and Enter Timestamp
downloadmedia - Download media to storage
storageinfo - Get Info about currently saved Files
clearffmpegmedia - Clear stored media from Telegram
generatecustomthumbnail - Generate customer thumbnail
generatescss - Get Screenshot of Telegram Media
```

- msg me on telegram Telegram.me/Avishkarpatil
