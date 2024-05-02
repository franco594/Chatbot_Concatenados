import google.generativeai as genai

genai.configure(api_key="AIzaSyCv4Bqhmilx9Bgia90_gz9AJDWcNv9MK8A")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
pregunta = ""

pares = [
    ['Hola', ['¡Hola!', '¿Cómo estás?']],
    ['Adiós', ['¡Hasta luego!', '¡Que tengas un buen día!']],
    ['Tengo una pregunta', ['Claro, adelante.']],
    ['(.*) clima (.*)', ['Puedes verificar el clima en línea.']],
    ['(.*) consejo (.*)', ['Intenta pensar en las cosas positivas de tu día.']],
    ['(.*)', ['Lo siento, no entiendo.']],
]

def respuesta():

    response = chat.send_message(pregunta)
    print(response.text)

while (True):
    pregunta = input("Ingrese su pregunta o ingrese Salir: ")

    if (pregunta.lower() == 'salir'):
        break
    else:
        respuesta()



