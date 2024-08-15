import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

TOKEN = '7321848780:AAE1ILkt2IwRnyXkQ9Xrl8LWRiujza8tHGY'

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Open",
                    web_app=WebAppInfo(url="https://github.com/BlackDrago0/BlackDrago0.git"),
                )
            ]
        ]
    )
    await message.answer(f"Hi, welcome to pepetap", reply_markup=markup)




@dp.message(Command('privacy'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"pricavy link")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
