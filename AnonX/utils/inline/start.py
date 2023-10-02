from typing import Union
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from config import SUPPORT_GROUP, SUPPORT_CHANNEL


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="★ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ★",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="★ ꜰᴇᴀᴛᴜʀᴇꜱ ★",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="★ ꜱᴇᴛᴛɪɴɢꜱ ★", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons

#extra shit
BOT_USERNAME = ("{BOT_USERNAME}")

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    global GROUP_USERNAME
    global CHANNEL_USERNAME
    buttons = [
        [
            InlineKeyboardButton(
                text="★ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ★",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="★ ᴄʜᴀɴɴᴇʟ ★", url=f"https://t.me/{SUPPORT_CHANNEL}",
            ),
        
            InlineKeyboardButton(
                text="★ ɢʀᴏᴜᴘ ★", url=f"https://t.me/{SUPPORT_GROUP}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="★ ꜰᴇᴀᴛᴜʀᴇꜱ ★", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
