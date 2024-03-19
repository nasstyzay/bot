from openai import OpenAI

# Замените {PROXY_API_KEY} на ваш реальный ключ API
client = OpenAI(
    api_key="{sk-8Xztn8PQF9mwTTTRnmNhfJveZJ0BgzWO}",
    base_url="https://api.openai.com",
)

def chat_with_ai():
    messages = []  # Список для хранения диалога

    print("Введите 'выход', чтобы прекратить общение.\n")

    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'выход':
            print("Общение завершено.")
            break

        # Добавляем пользовательский ввод в диалог
        messages.append({"role": "user", "content": user_input})

        # Запрос к нейросети
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages
        )

        # Получение и вывод ответа AI
        ai_message = response.choices[0].message['content']
        print("AI:", ai_message)

        # Добавляем ответ AI в диалог
        messages.append({"role": "assistant", "content": ai_message})

if __name__ == "__main__":
    chat_with_ai()