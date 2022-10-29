from aiogram.utils.callback_data import CallbackData

# Посмотреть товар, тут не нужен CallbackData
view_product = CallbackData("view", "id_product")

# Купить товар
buying_callback = CallbackData("buying", "id_product")

# Отменить покупку
cancellation_callback = CallbackData("cancellation", "id_product")