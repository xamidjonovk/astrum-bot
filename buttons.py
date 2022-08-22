from telegram import KeyboardButton, ReplyKeyboardMarkup

register_button = ReplyKeyboardMarkup([
    ["📋Ro'yhatdan o'tish"]
], resize_keyboard=True)

directory = ReplyKeyboardMarkup([
    ["💻Data Science", "💻Software Engineering"],
    ["💻Full Stack"]
], resize_keyboard=True)

seasons = ReplyKeyboardMarkup([
    ["👨‍🎓Season 1", "👨‍🎓Season 2"],
    ["👨‍🎓Season 3", "👨‍🎓Season 4"]
], resize_keyboard=True)

contact = [
    [KeyboardButton(text="📲Contact Yuborish", request_contact=True)]
]

check = ReplyKeyboardMarkup([
    ["✅Tasdiqlash"]
], resize_keyboard=True)

homework = ReplyKeyboardMarkup([
    ["📚Proyektni topshirish"], ["📚 Progress ko'rish 📖"]
], resize_keyboard=True, one_time_keyboard=True)

see_progress = ReplyKeyboardMarkup([
    ["📚 Progress ko'rish 📖"]
], resize_keyboard=True, one_time_keyboard=True)

qwasar_data = ReplyKeyboardMarkup([
    ["📚Get user data from qwasar"]
], resize_keyboard=True, one_time_keyboard=True)

admin_buttons = ReplyKeyboardMarkup([
    ["📈Statistika"], ["Statistikani yangilash"]
], resize_keyboard=True)
