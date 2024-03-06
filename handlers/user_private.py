import logging

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from filters.chat_types import ChatTypeFilter
import logging

FORMAT = '{asctime} : {funcName} - {levelname} - {msg}'
logging.basicConfig(filename='logger.log', filemode='a', encoding='UTF-8', format=FORMAT, style='{',
                    level=logging.NOTSET)
this_logger = logging.getLogger(__name__)

# Делим все события и их обработку на разные классы,
# например здесь мы делаем отдельный файл с роутером для переписки с пользователем.
# Его мы потом импортируем в наш основной файл и подключим к диспетчеру.
user_private_router = Router()
# добавляем собственный фильтр, что бот уже на этапе получения сообщения мог
# решить через какой роутер он должен его обработать
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    this_logger.warning(f'{message.from_user.username} запустил бота')
    await message.answer('Бот запущен!')


@user_private_router.message(Command("menu"))
async def menu_cmd_artem_v(message: types.Message):
    this_logger.info(f'{message.from_user.username} открыл "меню"')
    await message.answer('Menu: ')


@user_private_router.message(Command("about"))
async def about_cmd_artem_v(message: types.Message):
    this_logger.info(f'{message.from_user.username} открыл "о нас"')
    await message.answer('About: ')


@user_private_router.message(Command("other"))
async def other_cmd_artem_v(message: types.Message):
    this_logger.info(f'{message.from_user.username} открыл "другое"')
    await message.answer('Other: ')


@user_private_router.message(F.text)
async def magic_filter_artem_v(message: types.Message):
    this_logger.info(f'{message.from_user.username} написал {message.text}"')
    await message.answer("Ваше сообщение очень важно для нас, спасибо!.")
