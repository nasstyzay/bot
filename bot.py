import telebot
from openai import OpenAI

# ВАШ ТОКЕН ДЛЯ API OpenAI
OPENAI_API_KEY = "sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I"
# ВАШ ТОКЕН ДЛЯ ТЕЛЕГРАМ БОТА
TELEGRAM_BOT_TOKEN = "7041862910:AAFiVLmlYgzVqhtExprzq-Ud6OCMyUMT5kI"

# Инициализация клиента OpenAI
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcom(message):
    bot.reply_to(message, "Привет! Я Мася и использую нейронную сеть для ответов. Напиши мне что-нибудь :)")

def chat_with_ai(message_text):
    messages = [{"role": "user", "content": message_text}]
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
      )
    response_message = chat_completion.choices[0].message.content
    return response_message

@bot.message_handler(func=lambda message: True)
def echo_all (message):
    response = chat_with_ai(message.text)
    bot.reply_to(message, response)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)