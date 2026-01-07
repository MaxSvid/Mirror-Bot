from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)  

# Menu Buttons
main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='GeminiAI', callback_data='menu_gemini')],
        [InlineKeyboardButton(text='Job Reports', callback_data='menu_reports')],
        [InlineKeyboardButton(text='Crypto Alerts', callback_data='menu_alerts')],
        [InlineKeyboardButton(text='Settings', callback_data='menu_settings')]
        ])

# Back button
back_button = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Back", callback_data="menu_back")]
    ])

# Menu Options
gemini_options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Gemini Chat", callback_data="gemini_chat")],
    *back_button.inline_keyboard
    ])

reports_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="Overall", callback_data="reports_overall")]
    ])

alerts_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="Top 10 coins", callback_data="alerts_coins")]
    ])

settings_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="Bot GitHub", callback_data="settings_github")]
    ])
