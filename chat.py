# importar la libreria openai
import os
import openai
from dotenv import load_dotenv
load_dotenv()
api_chat1 = os.getenv("API_CHAT")

# Configurar la clave de API
openai.api_key = api_chat1
# variable para usar el api que tienes que sacar desde su pagina oficial
# creamos una variable vacia
conversation = ""
# variable para el contador
humano = input("ingrese tu nombre: ")
i = 1
# empezamos el ciclo para que inicie la conversación
while (i != 0):
    # ingresa el humano cualquier pregunta
    question = input(f"Pregunta-{humano} : ")
    # se ira acumulando los que va preguntando el humano
    conversation += "\nHumano " + question + "\nAI: "
    # La variable para que responda la IA
    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Humano:", " AI:"]
    )
    # almacena lo que saco en al hazar para responder
    anwer = response.choices[0].text.strip()
    # se ira acumulando la conversación
    conversation += anwer
    # Imprimimos lo que nos responde la IA
    print("Responde AI: " + anwer + "\n")
