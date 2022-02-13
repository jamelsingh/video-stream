""" inline section button """

from pyrogram import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  return [[
      InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data='cls'),
  ]]


def menu_markup(user_id):
  return [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'cbresume | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🗑 Close", callback_data='cls'),
    ]
  ]


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
