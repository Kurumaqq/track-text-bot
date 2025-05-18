from aiogram import Bot, Dispatcher
from aiogram.types import Message
from get_text import get_text
from dotenv import load_dotenv
import asyncio
from os import getenv

load_dotenv()
bot  = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher()
token = getenv('GENIUS_TOKEN')

@dp.message()
async def send_track_text(msg : Message):
    await msg.answer(get_text(msg.text, token))

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
