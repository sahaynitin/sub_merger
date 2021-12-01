from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select():
    upload_selection = [
        [
            InlineKeyboardButton(
                "Softmux",
                callback_data="transfersh"
            ),
            InlineKeyboardButton(
                "HardMux",
                callback_data="File.io"
            )
        ],
