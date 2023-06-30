from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup

def mainmenubutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton(text='🌮 Fast food'),
        KeyboardButton(text='🥤 Suvlar')
    )
    markup.add(
        KeyboardButton(text='🛍️ Buyurtmalarim'),
        KeyboardButton(text='🛒 Savatcha')
    )
    markup.add(
        KeyboardButton(text='☎️ Bog\'lanish')
    )
    return markup