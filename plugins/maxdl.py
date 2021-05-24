import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time
import urllib

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import progress_for_pyrogram
from helper_funcs.help_Nekmo_ffmpeg import take_screen_shot, cult_small_video

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser



@pyrogram.Client.on_message(pyrogram.filters.command(["maxdl"]))
async def maxdl_dl(bot, update):
    TRChatBase(update.from_user.id, update.text, "maxdl")
    saved_file_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".downloadlist.txt"
    if not os.path.exists(saved_file_path):
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id
        )
        try:
            c_time = time.time()
            await bot.download_media(
                message=update.reply_to_message,
                file_name=saved_file_path,
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.DOWNLOAD_START,
                    a,
                    c_time
                )
            )
        except (ValueError) as e:
            await bot.edit_message_text(
                chat_id=update.chat.id,
                text=str(e),
                message_id=a.message_id
            )
        for url in open('urls.txt'):
           name = url.rsplit('/', 1)[-1]
           filename = os.path.join(DOWNLOADS_DIR, name)
           if not os.path.isfile(filename):
              urllib.urlretrieve(url, filename)
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS,
            reply_to_message_id=update.message_id
        )
