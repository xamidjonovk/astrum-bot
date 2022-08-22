from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
import buttons as btn
from id import ADMIN_ID


def start_conversation(update, context):
    update.message.reply_text(text="*Talabaning qwasar usernameni kiriting*",
                              parse_mode="Markdown",
                              reply_markup=ReplyKeyboardRemove())
    return 1


def get_qwasar_name(update, context):
    message = update.message.text
    context.user_data['username'] = message

    from x import return_userdata
    username = context.user_data['username']

    if update.message['chat']['id'] == ADMIN_ID:
        try:
            update.message.reply_text(
                text=return_userdata(username),
                reply_markup=btn.see_progress
            )
        except:
            update.message.reply_text(
                text="Qandaydir xatolik mavjud",
                reply_markup=btn.see_progress
            )
    elif update.message['chat']['id'] != ADMIN_ID:
        try:
            update.message.reply_text(
                text=return_userdata(username),
                reply_markup=btn.homework
            )
        except:
            update.message.reply_text(
                text="Qandaydir xatolik mavjud !",
                reply_markup=btn.homework
            )

    return ConversationHandler.END
