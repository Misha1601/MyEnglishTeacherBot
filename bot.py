import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.echo import register_echo
from tgbot.handlers.user import register_user
from tgbot.middlewares.environment import EnvironmentMiddleware

# запускаем логгирование, логи выводятся только в консоль
logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    """Запуск мидлвари, раберусь позже"""
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    """Запуск запуск фильтров, разберусь позже"""
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    """Запуск хандлеров, порядок имеет значение"""
    register_admin(dp)
    register_user(dp)
    register_echo(dp)


async def main():
    """Асинхронный запуск главной функции"""
    #Выводим в консоль информацию о запуске скрипта
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    # Загружаем из .env настройки, шаблон настроек в .env_shablon
    config = load_config(".env")

    # Создаем объект бота и диспетчера
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot)

    # Загружаем в бота настройки, пока не разобрался в этом пункте
    bot['config'] = config

    # Отлавливаем сообщения прогоняя его по очереди
    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
