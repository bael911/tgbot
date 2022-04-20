from aiogram import executor
from config import dp
import logging
from handlers import callback, client, notic, fcmAdminGetUser,fcmAdminMenu
from database import bot_db


async def on_start_up(_):
    bot_db.sql_create()

client.register_hendlers_client(dp)
callback.register_hendlers_callback(dp)
# fcmAdminGetUser.register_hendler_fsmAdminGetUser(dp)
fcmAdminMenu.register_hendler_fsmAdminGetUser(dp)
notic.register_hendlers_notification(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False, on_startup=on_start_up)

