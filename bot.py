import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Токен бота (замени на свой!)
BOT_TOKEN ='8251195826:AAHFl8r3nFxht8URO-oFkfJve-LbSrkSMB0'

# URL твоего веб-приложения на Render
WEB_APP_URL = 'https://mono-telegram-webb.onrender.com/'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def send_welcome(message: types.Message):
    # Создаем WebApp кнопку
    web_app = WebAppInfo(url=WEB_APP_URL)
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="📚 Начать учить слова", web_app=web_app)
    ]])
    
    await message.answer(
        "Привет! 🎓\n\nДавай изучать английский с Mono! Нажми кнопку ниже чтобы начать:",
        reply_markup=keyboard
    )

async def main():
    print("Бот запущен! Иди в Telegram и проверяй /start")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
