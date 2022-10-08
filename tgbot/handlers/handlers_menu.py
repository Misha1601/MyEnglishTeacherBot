from aiogram import types
from bot import dp


# Событие нажатия на кнопку "выбрать товар"
@dp.message_handler(text="👀 Выбрать товар")
async def vibor_product(message: types.Message):
    await message.answer("Тут будет предложено выбрать категорию для просмотра товаров")

# Событие нажатия на кнопку "Корзина"
@dp.message_handler(text="🗑 Корзина")
async def vibor_product(message: types.Message):
    await message.answer("Тут будет отображен весь товар, который добавлен в корзину")

# Событие нажатия на кнопку "Мои заказы"
@dp.message_handler(text="🛒 Мои заказы")
async def vibor_product(message: types.Message):
    await message.answer("Тут будет отображен весь товар, которые заказаны и ожидают изготовления")

# Событие нажатия на кнопку "Новости"
@dp.message_handler(text="📢 Новости")
async def vibor_product(message: types.Message):
    await message.answer("Тут будет отображена информация, о которой могут узнать все")

# Событие нажатия на кнопку "Настройки"
@dp.message_handler(text="🔧 Настройки")
async def vibor_product(message: types.Message):
    await message.answer("Тут надо подумать. Настройки отображения для пользователей. И настройки для администратора")

# Событие нажатия на кнопку "Помощь"
@dp.message_handler(text="🚑 Помощь")
async def vibor_product(message: types.Message):
    await message.answer("Информация о боте, навигации по нему")