from aiogram.dispatcher.filters.state import State, StatesGroup

class DrinkState(StatesGroup):
    drink = State()