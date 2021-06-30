from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters

TG_TOKEN = "###"
TG_API_URL = "###"

from nah.config import load_config
from nah.utils import debug_requests
from logging import getLogger
config = load_config()
logger = getLogger(__name__)


@debug_requests
def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = "noname"

    text = update.effective_message.text
    reply_text = f"Hello, {name}\n\n {text}"

    bot.send_message(
        chat_id='1009310131',
        text=text
    )
    update.message.reply_text(
        text=reply_text
    )

def main():
    logger.info("Start bot..")
    bot = Bot(token=TG_TOKEN,
              base_url=TG_API_URL)
    updater = Updater(bot=bot)

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    # Проверить что бот корректно подключился к Telegram API
    info = bot.get_me()
    logger.info(f'Bot info: {info}')

    # Скачивать обновления с телеграмма
    updater.start_polling()
    # Работать до тех пор, пока программа не будет закрыта
    updater.idle()

    logger.info("Finish bot...")

if __name__ == '__main__':
    main()
