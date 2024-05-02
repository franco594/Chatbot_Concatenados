import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Lista de preguntas enumeradas
preguntas = [
    "1. ¿Cuál es tu nombre?",
    "2. ¿Cuál es tu edad?",
    "3. ¿Dónde vives?",
    "4. ¿Cuál es tu comida favorita?",
    "5. ¿Qué haces en tu tiempo libre?"
]

# Pares de patrones y respuestas para el chatbot
pares = [
    ('1', ['Mi nombre es Chatbot.']),
    ('2', ['Soy un programa de computadora, así que no tengo una edad específica.']),
    ('3', ['No tengo una ubicación física, existo en la red.']),
    ('4', ['Como soy un programa, no tengo una comida favorita.']),
    ('5', ['No tengo tiempo libre, estoy siempre aquí para ayudarte.']),
    ('adiós', ['¡Hasta luego!']),
    ('(.*)', ['Lo siento, no entiendo esa pregunta.']),
]

# Crear el chatbot
chatbot = Chat(pares, reflections)


# Función para enviar el mensaje
def enviar_mensaje():
    mensaje_usuario = entrada_usuario.get()
    chat_area.insert(tk.END, "Tú: " + mensaje_usuario + "\n")
    respuesta_chatbot = chatbot.respond(mensaje_usuario)
    chat_area.insert(tk.END, "Chatbot: " + respuesta_chatbot + "\n")
    entrada_usuario.delete(0, tk.END)


# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Chatbot de Consultas con NLTK y Tkinter")
root.geometry("400x500")

# Área de chat
chat_area = scrolledtext.ScrolledText(root, width=40, height=20)
chat_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Lista de preguntas
preguntas_label = tk.Label(root, text="Preguntas:")
preguntas_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
preguntas_listbox = tk.Listbox(root, width=30, height=5)
for pregunta in preguntas:
    preguntas_listbox.insert(tk.END, pregunta)
preguntas_listbox.grid(row=1, column=1, padx=10, pady=10)

# Entrada de usuario
entrada_usuario = tk.Entry(root, width=30)
entrada_usuario.grid(row=2, column=0, padx=10, pady=10)

# Botón de enviar
boton_enviar = tk.Button(root, text="Enviar", command=enviar_mensaje)
boton_enviar.grid(row=2, column=1, padx=10, pady=10)


# Función para cerrar la ventana
def cerrar_ventana():
    root.destroy()


# Configuración del cierre de la ventana
root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Ejecutar la aplicación
root.mainloop()
