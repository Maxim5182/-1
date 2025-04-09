import telebot




bot = telebot.TeleBot("7944496837:AAGUaO7twXzauXCS0otPwC5V7prCHoYfuIo")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['plastic'])
def send_plastic(message):  
        bot.reply_to(message, "Пластик разлагается около 1 тыс. лет") 

@bot.message_handler(commands=['paper'])
def send_paper(message):  
        bot.reply_to(message, "Бумага разлагается около 2-х лет") 

@bot.message_handler(commands=['glass'])
def send_glass(message):  
        bot.reply_to(message, "Стекло разлагается около 1000 лет")


@bot.message_handler(commands=['rubber'])
def send_rubber(message):  
        bot.reply_to(message, "Резина разлагается око 120-140 лет")

@bot.message_handler(commands=['species'])
def send_species(message):  
        bot.reply_to(message, "желтый – пластик; зеленый – несортированные коммунальные отходы; оранжевый – опасные отходы; синий – макулатура; красный – стекло; серый – электрооборудование, вышедшее из строя.")
