from aiogram import Bot, Dispatcher, types, executor

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config

bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('🇺🇸 Welcome to your Dark Side. Just send any text message and it will be retranslated anonymously to our channel.\n🇷🇺 Добро пожаловать на темную сторону. Просто отправьте любое текстовое сообщение, и оно будет передано анонимно в общий канал.')

@dp.message_handler(content_types=['new_chat_members'])
async def on_user_join(message: types.Message):
    await message.delete()

@dp.message_handler(content_types=['left_chat_member'])
async def on_user_leave(message: types.Message):  
    await message.delete()

@dp.message_handler()
async def mainfunc(message: types.Message):  
    if message.chat.type == 'private':
        try:
            await bot.send_message(config.chatid, message.text)
        except:
            await message.reply('🇺🇸 Only text is supported.\n🇷🇺 Поддерживаются лишь текстовые сообщения.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
