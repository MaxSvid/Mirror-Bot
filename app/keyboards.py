from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)  

# Menu Buttons
main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='GeminiAI')],
                                    [KeyboardButton(text='Job Reports')],
                                    [KeyboardButton(text='Crypto Alerts')],
                                    [KeyboardButton(text='Settings')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Choose the options...')

gemini_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Gemini Chat', 
                                                                             callback_data='gemini_chat')],                                             
                                                ])

reports_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Overall', 
                                                                              callback_data='reports_overall')],                                             
                                                ])

alerts_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Top 10 Coins', 
                                                                              callback_data='alerts_coins')],                                             
                                                ])

settings_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Bots GitHub Link', 
                                                                              callback_data='settings_github')],                                             
                                                ])
