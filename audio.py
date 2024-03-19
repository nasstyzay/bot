from openai import OpenAI
import telebot
from gtts import gTTS
import os

TELEGRAM_BOT_TOKEN = "7041862910:AAFiVLmlYgzVqhtExprzq-Ud6OCMyUMT5kI"
OPENAI_API_KEY = "sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I"

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1"
)

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Мася и я хомяк. Я люблю общаться обо всём на свете :)")


def chat_with_ai(message_text):
    messages = [{"role": "user", "content": message_text}]
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
      )
    response_message = chat_completion.choices[0].message.content
    return response_message

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = chat_with_ai(message.text)

    tts = gTTS(response, lang='ru')
    tts.save("response.mp3")

    with open("response.mp3", "rb") as audio:
        bot.send_voice(message.chat.id, audio)

    os.remove("response.mp3")

if __name__ == "__main__":
    bot.infinity_polling()