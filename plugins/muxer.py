from pyrogram import Client, filters
from helper_func.progress_bar import progress_bar
from helper_func.dbhelper import Database as Db
from helper_func.mux import softmux_vid, hardmux_vid
from config import Config
from plugins.forcesub import handle_force_subscribe
import time
import os
db = Db()

@Client.on_message(filters.command('softmux') & filters.private)
async def softmux(bot, message, cb=False):
    


