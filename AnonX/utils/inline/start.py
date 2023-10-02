from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


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
                text="★ ʜᴇʟᴘ ★",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="★ ꜱᴇᴛᴛɪɴɢꜱ ★", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="★ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ★",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="★ ᴏᴡɴᴇʀ ★", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="★ ʜᴇʟᴘ ★", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="★ ɢʀᴏᴜᴘ ★", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="★ ᴄʜᴀɴɴᴇʟ ★", url=f"https://t.me/BRANDRD_BOT",
            )
        ],
        [
            InlineKeyboardButton(
                text="★ ʀᴇᴘᴏ ★",
                url=f"https://github.com/KrishnaxMusic/BRANDED-MASTI",
            )
        ],
     ]
    return buttons
