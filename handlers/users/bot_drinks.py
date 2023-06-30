from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.default.mainmenubuttons import *
from keyboards.default.categories import *
from states.drinkstate import *


@dp.message_handler(text='🥤 Suvlar')
async def drinkcategory(message: Message):
    await message.answer('Kategoriyani tanlang', reply_markup=drinkscategorybutton())
    await DrinkState.drink.set()


@dp.message_handler(state=DrinkState.drink)
async def getdrink(message: Message, state: FSMContext):
    drink = message.text
    if drink == '⬅️ Orqaga' or drink == '/start':
        await message.answer('Bosh menu', reply_markup=mainmenubutton())
    elif drink == '🥤 Coca cola':
        image = open('196_coca-cola-05-litra.jpg', 'rb')

        text = f'Coca cola 1 litr\n\n' \
               f'Narxi: 9 000 so\'m'

        await message.answer_photo(photo=image, caption=text)

    elif drink == '🥤 Pepsi':
        image = open('Napitok_Gazirovannyy_PEPSI_05_l.650@2x.jpg', 'rb')

        text = f'Pepsi 1 litr\n\n' \
               f'Narxi: 9 000 so\'m'

        await message.answer_photo(photo=image, caption=text)
    elif drink == '🥤 Fanta':

        image = open('Напиток_FANTA_Апельсин_0_5_л_пл.jpg', 'rb')

        text = f'Fanta 1 litr\n\n' \
               f'Narxi: 8 000 so\'m'

        await message.answer_photo(photo=image, caption=text)
    elif drink == '🥤 Dena':

        image = open('dena.jpg', 'rb')

        text = f'Dena 1 litr\n\n' \
               f'Narxi: 11 000 so\'m'

        await message.answer_photo(photo=image, caption=text)

    elif drink == '🥤 Dinay':

        image = open('dinay-vishnya-1l.jpg', 'rb')
        text = f'Dinay 1 litr\n\n' \
               f'Narxi: 12 000 so\'m'

        await message.answer_photo(photo=image, caption=text)
