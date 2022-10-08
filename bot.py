import logging
from aiogram import Bot, Dispatcher, executor, types
from tgbot.config import load_config


# запускаем логгирование, логи выводятся только в консоль
logging.basicConfig(level=logging.INFO)

# Загружаем из .env настройки, шаблон настроек в .env_shablon
config = load_config(".env")
# Создаем объект бота и диспетчера
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(bot)


if __name__=="__main__":
    # from tgbot.handlers.admin import dp
    # from tgbot.handlers.echo import dp
    # from tgbot.handlers.user import dp
    from tgbot.handlers.handlers import dp # Команда start
    from tgbot.handlers.handlers_menu import dp # События на нажатия меню

    # from handlers.handlers import dp # Команда start
    # from handlers.handlers_menu import dp # События на нажатия меню
    # from handlers import dp # Команда info
    # from app.handlers.show_follows import dp # Команда выводит подписки если они есть (вывод всех заказов)
    # from app.handlers.stop import dp # Команда stop
    # from app.handlers.buying_product import dp # События на добавление новой подписки (добавление нового заказа)
    # from app.handlers.unfollow import dp # Событие на удаление подписка (отменить заказ)
    executor.start_polling(dp, skip_updates=True)
