import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Pares de patrones y respuestas para el chatbot
pares = [
    ('mi nombre es (.*)', ['Hola %1, ¿cómo puedo ayudarte hoy?']),
    ('(Hola|Hola!|Hola.)', ['Hola, ¿en qué puedo ayudarte?']),
    ('¿Cómo estás?', ['Estoy bien, gracias. ¿Y tú?']),
    ('(.*) ayuda (.*)', ['Claro, ¿en qué necesitas ayuda?']),
    ('adiós', ['¡Hasta luego!']),
    ('(.*)', ['Lo siento, no entiendo.']),
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
root.title("Chatbot con NLTK y Tkinter")
root.geometry("400x400")

# Área de chat
chat_area = scrolledtext.ScrolledText(root, width=40, height=20)
chat_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Entrada de usuario
entrada_usuario = tk.Entry(root, width=30)
entrada_usuario.grid(row=1, column=0, padx=10, pady=10)

# Botón de enviar
boton_enviar = tk.Button(root, text="Enviar", command=enviar_mensaje)
boton_enviar.grid(row=1, column=1, padx=10, pady=10)


# Función para cerrar la ventana
def cerrar_ventana():
    root.destroy()


# Configuración del cierre de la ventana
root.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Ejecutar la aplicación
root.mainloop()
