from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
import buttons as btn
import pandas as pd
from id import ADMIN_ID


def start_conversation(update, context):
    update.message.reply_text(text="*Project nomini kiritng*",
                              parse_mode="Markdown",
                              reply_markup=ReplyKeyboardRemove())
    return 1


def get_project_name(update, context):
    message = update.message.text
    context.user_data['project_name'] = message

    update.message.reply_text(
        text="*Project uchun feed back kiritng*:",
        parse_mode="Markdown")
    return 2


def get_feedback(update, context):
    message = update.message.text
    context.user_data['feedback'] = message

    update.message.reply_text(
        text="*Project fileni yuboring*:",
        parse_mode="Markdown")
    return 3


def get_fileid(update, context):
    context.user_data['file_id'] = update.message['document']['file_id']

    update.message.reply_text(
        text="*Projectni tasdiqlang*:",
        parse_mode="Markdown",
        reply_markup=btn.check)
    return 4


def submit(update, context):
    project_name = context.user_data['project_name']
    feedback = context.user_data['feedback']
    file_id = context.user_data['file_id']

    data = pd.read_csv('database.csv')

    data = data[data['user_id'] == update.message.from_user.id]

    qwasar_username = data['qwasar_username'].values[0]
    firstname = data['firstname'].values[0]
    lastname = data['lastname'].values[0]
    contact = data['contact'].values[0]
    season = data['season'].values[0]
    study = data['study'].values[0]
    telegram_username = update.message.from_user.username
    user_id = update.message.from_user.id

    # print(update.message['chat']['id'])

    context.bot.sendDocument(chat_id=ADMIN_ID,
                             caption=f"\nproject name : *{project_name}*\n\n"
                                     f"project feedback : *{feedback}*\n\n"
                                     f"About : \n"
                                     f"qwasar username : {qwasar_username}\n"
                                     f"firstname : {firstname}\n"
                                     f"lastname : {lastname}\n"
                                     f"contact : {contact}\n"
                                     f"season : {season}\n"
                                     f"study : {study}\n"
                                     f"telegram username : @{telegram_username}\n"
                                     f"user_id : {user_id}\n",
                             document=file_id)

    update.message.reply_text(
        text="*Project tasdiqlandi*",
        parse_mode="Markdown",
        reply_markup=btn.homework
    )
    return ConversationHandler.END
