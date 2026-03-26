import asyncio
import io
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from PIL import Image, ImageDraw, ImageFont
from aiohttp import web

# Токен берем из переменных окружения (безопасность!)
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Твой старый код генерации картинки (сокращенно) ---
def create_recipe_image(text):
    # (Весь тот код с Pillow, который мы писали выше)
    # ... (просто вставь функцию целиком сюда) ...
    return buf # возвращает io.BytesIO()

@dp.message()
async def handle(message: types.Message):
    if message.text:
        img = create_recipe_image(message.text)
        await message.answer_photo(photo=types.BufferedInputFile(img.read(), filename="note.png"))

# --- Хитрый ход для Render: Веб-сервер ---
async def handle_web(request):
    return web.Response(text="Bot is alive!")

async def main():
    # Запускаем веб-сервер на порту, который даст Render
    app = web.Application()
    app.router.add_get("/", handle_web)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv("PORT", 8080)))
    await site.start()
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
