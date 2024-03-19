from telebot import TeleBot  # Исправленный импорт

# Ваш токен от BotFather (замените на реальный токен бота)
TOKEN = '7041862910:AAFiVLmlYgzVqhtExprzq-Ud6OCMyUMT5kI'
bot = TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Мася, милый хомячок. Я создан(а) для команд /start, /help, /perevorot, /caps, /cut_gl, /cut_sogl, /rus, /chet, /LoLkEk")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """
Список команд:
/start - приветствие
/help - список команд и описание
/perevorot - переворот вашего сообщения
/caps - преобразование текста в заглавные буквы
/cut_gl - удаление гласных букв из текста
/cut_sogl - удаление согласных букв из текста
/rus - перевод текста с английской расскладки на русскую
/chet - подсчет количества символов в тексте
/LoLkEk - чередование заглавных и маленьких букв в тексте
""")
# Обработчик команды /perevorot
@bot.message_handler(commands=['perevorot'])
def perevorot(message):
    if len(message.text.split()) > 1:
        text_to_reverse = ' '.join(message.text.split()[1:])
        reversed_text = text_to_reverse[::-1]
        bot.reply_to(message, reversed_text)
    else:
        bot.reply_to(message, "Пожалуйста, добавь текст после команды /perevorot. Например: /perevorot текст")

# Обработчик команды /caps
@bot.message_handler(commands=['caps'])
def caps(message):
    if len(message.text.split()) > 1:
        text_to_caps = ' '.join(message.text.split()[1:])
        caps_text = text_to_caps.upper()
        bot.reply_to(message, caps_text)
    else:
        bot.reply_to(message, "Пожалуйста, добавь текст после команды /caps. Например: /caps пример текста")

# Обработчик команды /cut_gl
@bot.message_handler(commands=['cut_gl'])
def cut_gl(message):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU' # Список гласных букв для удаления
    if len(message.text.split()) > 1:
        text_to_cut = ' '.join(message.text.split()[1:])
        text_without_vowels = ''.join([char for char in text_to_cut if char not in vowels])
        bot.reply_to(message, text_without_vowels)
    else:
        bot.reply_to(message, "Пожалуйста, добавь текст после команды /cut_gl. Например: /cut_gl ваш текст")

# Обработчик команды /cut_sogl
@bot.message_handler(commands=['cut_sogl'])
def cut_sogl(message):
    consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' # Список согласных букв для удаления
    if len(message.text.split()) > 1:
        text_to_cut = ' '.join(message.text.split()[1:])
        text_without_consonants = ''.join([char for char in text_to_cut if char not in consonants])
        bot.reply_to(message, text_without_consonants)
    else:
        bot.reply_to(message, "Пожалуйста, добавь текст после команды /cut_sogl. Например: /cut_sogl ваш текст")

translit_dict = {
    'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е', 'z': 'з',
    'i': 'и', 'j': 'й', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
    'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'h': 'х',
    'c': 'ц', 'y': 'ы', 'x': 'х', 'w': 'в', 'q': 'к', '`': '`', ' ': ' ',
    '[': 'х', ']': 'ъ', ';': 'ж', "'": 'э', ',': 'б', '.': 'ю', '/': '.',
    '{': 'Х', '}': 'Ъ', ':': 'Ж', '"': 'Э', '<': 'Б', '>': 'Ю', '?': ',',
    '~': '-', '@': '"', '#': '№', '$': ';', '^': ':', '&': '?', '|': '/'
}

# Функция перевода текста с английской раскладки на русский язык
def transliterate(text, dictionary):
    return ''.join([dictionary.get(char, char) for char in text.lower()])

# Обработчик команды /rus
@bot.message_handler(commands=['rus'])
def rus(message):
    if len(message.text.split()) > 1:
        text_to_transliterate = ' '.join(message.text.split()[1:])
        transliterated_text = transliterate(text_to_transliterate, translit_dict)
        bot.reply_to(message, transliterated_text)
    else:
        bot.reply_to(message, "Пожалуйста, введите текст после команды /rus. Например: /rus ghbdtn")

import re

# Обработчик команды /chet
@bot.message_handler(commands=['chet'])
def chet(message):
    if len(message.text.split()) > 1:
        text = ' '.join(message.text.split()[1:])
        letters_count = len(re.findall(r'\w', text))
        words_count = len(text.split())
        sentences_count = len(re.split(r'[.!?]', text)) - 1  # Вычитаем один, так как split добавит пустую строку в конце

        response_message = f"В вашем тексте:\nБукв: {letters_count}\nСлов: {words_count}\nПредложений: {sentences_count}"
    else:
        response_message = "Пожалуйста, добавьте текст после команды /chet. Например: /chet Сколько слов в этом предложении?"

    bot.reply_to(message, response_message)

# Обработчик команды /LoLkEk
@bot.message_handler(commands=['LoLkEk'])
def lolk_text(message):
    if len(message.text.split()) > 1:
        # Получаем текст, кроме самой команды
        text = ' '.join(message.text.split()[1:])
        # Применяем функцию чередования регистра к каждому символу в тексте
        result = ''.join(
            char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)
        )
        bot.reply_to(message, result)
    else:
        bot.reply_to(message, "Пожалуйста, добавьте текст после команды /LoLkEk. Например: /LoLkEk пример текста")

# Остальные обработчики команд...

# Запуск бота и его опрос сервера на предмет новых сообщений
bot.polling()

