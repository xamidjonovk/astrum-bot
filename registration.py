from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
import buttons as btn
from add_to_database import add_to_base as add
import pandas as pd


def start_conversation(update, context):
    update.message.reply_text(text="*Qwasar platformasidagi usernamingizni kiriting*",
                              parse_mode="Markdown",
                              reply_markup=ReplyKeyboardRemove())
    return 1


def get_qwasar_username(update, context):
    message = update.message.text
    context.user_data['qwasar_username'] = message

    update.message.reply_text(
        text="*Ismingizni kiriting*:",
        parse_mode="Markdown")
    return 2


def get_firstname(update, context):
    message = update.message.text
    context.user_data['firstname'] = message

    update.message.reply_text(
        text="*Familiyangizni kiriting*:",
        parse_mode="Markdown")
    return 3


def get_lastname(update, context):
    message = update.message.text
    context.user_data['lastname'] = message

    update.message.reply_text(
        text="*Telefon raqamingizni yuboring*",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardMarkup(btn.contact, resize_keyboard=True)
    )
    return 4


def get_contact(update, context):
    message = update.message.text
    context.user_data["contact"] = update.message.contact.phone_number

    update.message.reply_text(
        text="*Qaysi seasonda o'qishingizni tanlang*:",
        reply_markup=btn.seasons,
        parse_mode="Markdown")
    return 5


def get_season_num(update, context):
    message = update.message.text
    context.user_data["season"] = message

    update.message.reply_text(
        text="*Yo'nalishingizni tanlang*:",
        reply_markup=btn.directory,
        parse_mode="Markdown")
    return 6


def get_study_type(update, context):
    message = update.message.text
    context.user_data["study"] = message

    qwasar_username = context.user_data['qwasar_username']
    firstname = context.user_data['firstname']
    lastname = context.user_data['lastname']
    contact = context.user_data['contact']
    season = context.user_data['season']
    study = context.user_data['study']

    update.message.reply_text(
        text=f"Ma'lumotlaringizni tekshiring va to'griligini tasdiqlang \n"
             f"\nQwasar username: *{qwasar_username}* \n"
             f"\nIsm: *{firstname}* \n"
             f"\nFamiliya: *{lastname}* \n"
             f"\nTelefon raqam: *{contact}* \n"
             f"\nSeason: *{season}* \n"
             f"\nYo'nalish: *{study}* \n",
        parse_mode="Markdown",
        reply_markup=btn.check
    )
    return 7


def submit(update, context):

    qwasar_username = context.user_data['qwasar_username']
    firstname = context.user_data['firstname']
    lastname = context.user_data['lastname']
    contact = context.user_data['contact']
    season = context.user_data['season']
    study = context.user_data['study']
    telegram_username = update.message.from_user.username
    user_id = update.message.from_user.id

    real_data = pd.read_csv('database.csv')
    add(real_data, qwasar_username, firstname, lastname, contact, season, study, telegram_username, user_id)

    from id import ADMIN_ID

    if update.message.from_user.id == ADMIN_ID:
        update.message.reply_text(
            text="Ro'yhatdan muvaffaqiyatli o'tdingiz",
            parse_mode="Markdown",
            reply_markup=btn.see_progress)
    else:
        update.message.reply_text(
            text="Ro'yhatdan muvaffaqiyatli o'tdingiz",
            parse_mode="Markdown",
            reply_markup=btn.homework
        )
    return ConversationHandler.END

