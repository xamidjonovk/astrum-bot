from telegram.ext import Filters
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler
import buttons as btn
import registration as rg
import send_project as sp
import get_user_data as gud


def start(update, context):
    user = update.message.from_user.first_name
    update.message.reply_text(f"Salom *{user}* \n"
                              f"*Botdan foydalanish uchun ro'yhatdan o'ting*",
                              reply_markup=btn.register_button,
                              parse_mode="Markdown")


def feed_back(update, context):
    if update.message.text.strip()[0:5] == "#feed":
        context.bot.sendDocument(
            chat_id=update.message['reply_to_message']['caption'].split("\n")[-1].split(":")[-1].strip(),
            caption=f"{update.message['reply_to_message']['caption']}\n\n\n*Tekshirildi*\n*#feedback : {update.message.text.replace('#feed', '')}",
            document=update.message['reply_to_message']['document']['file_id'])
        update.message.reply_text(f"*Project tekshirildi !*")

    # elif update.message.text.strip()[0:5] == "#user":
    #     user_name = str(update.message.text.strip()[5:]).strip()
    #     from x import return_userdata
    #     update.message.reply_text(f"{return_userdata(user_name)}")
    #
    # else:
    #     update.message.reply_text(f"*Qandaydir hatolik mavjud !*")


def main():
    updater = Updater(token="5515845639:AAG8jcmMf4Vxt_2LrEGeoOutaj3zUwcV660")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex('(Ro\'yhatdan o\'tish)'), rg.start_conversation)],
            states={
                1: [MessageHandler(Filters.text, rg.get_qwasar_username)],
                2: [MessageHandler(Filters.text, rg.get_firstname)],
                3: [MessageHandler(Filters.text, rg.get_lastname)],
                4: [MessageHandler(Filters.contact, rg.get_contact)],
                5: [MessageHandler(Filters.text, rg.get_season_num)],
                6: [MessageHandler(Filters.text, rg.get_study_type)],
                7: [MessageHandler(Filters.text, rg.submit)],
            },
            fallbacks=[CommandHandler('stop', start)]
        )
    )

    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex('(Proyektni topshirish)'), sp.start_conversation)],
            states={
                1: [MessageHandler(Filters.text, sp.get_project_name)],
                2: [MessageHandler(Filters.text, sp.get_feedback)],
                3: [MessageHandler(Filters.document, sp.get_fileid)],
                4: [MessageHandler(Filters.text, sp.submit)],
            },
            fallbacks=[CommandHandler('stop', start)]
        )
    )

    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[MessageHandler(Filters.regex("(Progress ko'rish)"), gud.start_conversation)],
            states={
                1: [MessageHandler(Filters.text, gud.get_qwasar_name)],
            },
            fallbacks=[CommandHandler('stop', start)]
        )
    )

    dispatcher.add_handler(MessageHandler(Filters.text, feed_back))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi")
    main()
