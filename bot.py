
import asyncio

from aiogram import Router, Bot, Dispatcher
from aiogram.client import bot
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder


def webapp_builder() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Let's Click!", web_app=WebAppInfo(
            url=""
        )
    )
    return builder.as_markup()


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(
        "Click! Click! Click",
        reply_markup=webapp_builder()
    )


async def main() -> None:
    bot = Bot("", parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await bot.start_polling(bot)

    if __name__ == '__main__':
        asyncio.run(main())
