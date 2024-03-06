import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv

# прячем наш токен в .env файл, и потом достаем его следующей командой:
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from common.bot_cmds_list import private

# здесь указываем список адейтов на которые наш бот должен как то реагировать.
# Все остальное нам не нужно, поэтому мы их записали что бы не нагружать скрипт.
ALLOWED_UPDATES = ['message', 'edited_message', 'command']

# Инициализируем класс самого бота, для этого нужен токен
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()

# Тут мы подключаем роутер из handlers к нашему диспетчеру.
dp.include_router(user_private_router)


# При помощи асинхронной функции, запускаем наш бот в работу.
# Запуск идет через метод await, с его помощью бот бесконечно будет спрашивать
# сервер телеграма на наличие новых сообщений для бота.
async def main():
    # Пишем следующую команду, что бы в случае отключения бота, он не начал отвечать на все сообщения,
    # которые ему отправлялись пока он был офлайн.
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


# Тут запускаем бота в работу.
asyncio.run(main())
