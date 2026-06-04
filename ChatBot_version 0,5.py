import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError("A chave GROQ_API_KEY não foi encontrada nas variáveis de ambiente.")

client = Groq(api_key=api_key)
user_message = input("Digite sua mensagem para o Chat: ")

def testar_conexao_groq(user_message):
    system = False
    try:
        print("Enviando solicitação...")
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_message}],
            model="llama-3.3-70b-versatile",
        )
        print(f"Resposta: {chat_completion.choices[0].message.content}")
        user_system = input("Deseja continuar?")
        if user_system == "S":
            system = True
        else:
            system = False
        while user_message and system:
            user_message = input("Digite sua mensagem para o Chat: ")
            testar_conexao_groq(user_message)
    except Exception as e:
        print(f"Erro: {e}")
if __name__ == "__main__":
    testar_conexao_groq(user_message)