import datetime
import json
from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import hbold ,hlink
from conf import TOKEN
from aiogram.dispatcher.filters import Text
from aiogram import executor
import logging

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)






@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_button = ["Все новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)

    await message.answer("Лента новостей", reply_markup=keyboard)




@dp.message_handler(Text(equals="news"))
async def get_all_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
          news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                 f"{hlink(v['article_title'], v['article_url'])}"

          await message.answer(news)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
