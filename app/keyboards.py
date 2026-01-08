from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)  

# Menu Buttons
main = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='GeminiAI', callback_data='menu_gemini')],
        [InlineKeyboardButton(text='Job Reports', callback_data='reports_menu')],
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

reports_options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="24h Overall", callback_data="reports_overall")],
    [InlineKeyboardButton(text="Developers Report", callback_data="dev_reports")],
    [InlineKeyboardButton(text="DS/DA's Report", callback_data="dsa_reports")],
    [InlineKeyboardButton(text="UK Jobs Report", callback_data="dsa_reports")],
    [InlineKeyboardButton(text="Websites", callback_data="websites_links")],
    *back_button.inline_keyboard
    ])

alerts_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="Top 10 coins", callback_data="alerts_coins")],
    [InlineKeyboardButton(text="DeFi", callback_data="defi_alerts")],
    [InlineKeyboardButton(text="Sources", callback_data="sources_alerts")],
    *back_button.inline_keyboard
    ])

settings_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text="Bot GitHub", url="https://github.com/MaxSvid/Mirror-Bot")],
    *back_button.inline_keyboard
    ])
