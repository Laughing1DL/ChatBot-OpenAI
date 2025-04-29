import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Almacena historial de conversación como lista de mensajes
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program.")
print("Type 'new' to switch conversation thread.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        break
    elif user_message.lower() == "new":
        conversation_history = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        print("New conversation thread started.\n")
        continue

    # Añadir mensaje del usuario al historial
    conversation_history.append({"role": "user", "content": user_message})

    # Enviar a la API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    reply = response.choices[0].message.content.strip()
    print(f"GPT: {reply}\n")

    # Añadir respuesta de la IA al historial
    conversation_history.append({"role": "assistant", "content": reply})