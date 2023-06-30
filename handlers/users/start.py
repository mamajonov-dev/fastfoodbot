from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.mainmenubuttons import *

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!"
                         f" Fast food buyurtma qilish botiga xush kelibsiz!", reply_markup=mainmenubutton())
