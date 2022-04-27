from aiogram import types, Dispatcher
from config import bot, dp
import asyncio
import aioschedule
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
#
# async def wake_up():
#     await bot.send_message(chat_id=chat_id, text="Эржан вставай !")


# async def scheduler(time):
#     aioschedule.every().day.at(time).do(wake_up)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)


# @dp.message_handler()
async def echo_message(message: types.Message):
    global chat_id
    chat_id = message.chat.id

    # Check bad words
    bad_words = "java bitch дурак балбес эшек".split()

    for i in bad_words:
        if i in message.text.lower():
            await message.delete()
            await bot.send_message(message.chat.id,
                           f"{message.from_user.full_name}, сам ты {i}!!!"
                           )

    # Send dice
    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji="🎯")
    if message.text.startswith('Разбуди меня в'," "):
        await message.reply("Ок!")
        await scheduler(message.text.replace())

def register_hendlers_notification(dp: Dispatcher):
    dp.register_message_handler(echo_message)