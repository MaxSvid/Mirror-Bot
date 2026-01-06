from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)  

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='GeminiAI')],
                                    [KeyboardButton(text='Job Reports')],
                                    [KeyboardButton(text='Crypto Alerts')],
                                    [KeyboardButton(text='Settings')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Choose the options...')

gemini_options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Gemini Chat', callback_data='gemini_chat')],                                             
                                                ])
