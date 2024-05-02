import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Pares de patrones y respuestas para el chatbot
pares = [
    ('hola|ayuda', ['Hola, en que puedo ayudarte?']),

    ('menu|Menu', ['MENU:\n'
                   '1. Torneos\n'
                   '2. Horarios\n'
                   '3. Reglas']),

    ('1', ['Los torneos disponibles son:\n'
           'bla, bla']),

    ('2', ['Los horarios son:\n'
           'bla, bla PM']),

    ('3', ['Las reglas son:\n'
           '1. bla\n'
           '2. bla']),

    ('adiós', ['¡Hasta luego!']),
    ('(.*)', ['Lo siento, no entiendo esa pregunta.']),
]

# Crear el chatbot
chatbot = Chat(pares, reflections)

# Mensaje de bienvenida
mensaje_bienvenida = ("¡Hola! Soy un Chatbot. ¿En qué puedo ayudarte?\n"
                      "MENU:\n"
                      "1. Torneos\n"
                      "2. Horarios\n"
                      "3. Reglas")


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
root.geometry("500x400")

# Área de chat
chat_area = scrolledtext.ScrolledText(root, width=58, height=20)
chat_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
chat_area.insert(tk.END, "Chatbot: " + mensaje_bienvenida + "\n")  # Mostrar mensaje de bienvenida

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
