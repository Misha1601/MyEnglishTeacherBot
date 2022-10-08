from aiogram import types
# from aiogram import SendPhoto
# from aiogram.utils.markdown import hbold, hlink
from bot import dp
# from tgbot.keyboards.keyboards import buttons_product
from tgbot.keyboards.keyboards_menu import buttons_menu


@dp.message_handler(commands="start")
async def start(message: types.Message):
    # a = message.from_user
    # b = message
    # print(a)
    # print(b)
    await message.answer("Добро пожаловать в бота для покупки товаров ручной работы\n"
                        "Для получения информации о возможностях бота используйте команду /info",
                        reply_markup=buttons_menu())

@dp.message_handler(commands="info")
async def info(message: types.Message):
    await message.answer("Чтобы посмотреть товары используйте команду /product \n" # /start
                         "Чтобы посмотреть товар с фото /product1 \n")

# @dp.message_handler(commands="product")
# async def info(message: types.Message):
#     products = db.product()
#     for product in products:
#         product = f'{hbold("Название: ", product[1])}\n' \
#            f'{hbold("Цена: ", product[2])}\n' \
#         #    f'{hbold("Фото: ", product[3])}'
#         await message.answer(product, reply_markup=buttons_product(product[0]))

# myfileid = []

# @dp.message_handler(commands="product1")
# async def info(message: types.Message):
#     # проверяем есть ли file_id у данной картинки в БД,
#     # если есть, вместо фото подставляем его
#     # если нет, отправляем фото и сохраняем file_id в БД
#     # photo = types.InputFile("foto_product/21.jpg")
#     # id_photo = await message.answer_photo(photo)
#     # print(id_photo)
#     # id = id_photo['photo'][0]['file_id'] # это сам file_id
#     # print(id)
#     await message.answer_photo('AgACAgIAAxkDAAIDkGMS4GoY459N4xgzu9OGWeONlWjeAALYvzEbzj-QSHMPOw_ivA8DAQADAgADcwADKQQ',
#                                 caption="пример подписи к фото")
#     await message.answer_photo('AgACAgIAAxkDAAIFA2MYFi2T2EVAT9JntD4NhodRk4q8AALWuzEbvB_ASLvnOUmz6co-AQADAgADcwADKQQ',
#                                 caption="пример подписи к фото2")
