import tkinter as tk
from tkinter import font
from nltk.chat.util import Chat, reflections
from training import pares, mensaje_bienvenida

# Crear el chatbot
chatbot = Chat(pares, reflections)


def send_message(event=None):
    user_message = user_input.get()
    if user_message.strip():
        display_message(user_message, "user")
        user_input.set("")
        # Obtener una respuesta del chatbot
        bot_response = chatbot.respond(user_message)
        display_message(bot_response, "bot")


def display_message(message, sender):
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Calcular la posición y la altura de los mensajes anteriores
    y = sum([canvas.bbox(item[0])[3] - canvas.bbox(item[0])[1] for item in messages]) + 10
    message_font = font.Font(family="Arial", size=12)
    sender_font = font.Font(family="Arial", size=10, weight="bold")

    if sender == "user":
        sender_text = "Tú: "
        fill_color = "#add8e6"
        text_color = "blue"
        x = 500 - message_font.measure(message + sender_text) - 40
    else:
        sender_text = "Bot: "
        fill_color = "#90ee90"
        text_color = "green"
        x = 10

    # Añadir el remitente
    sender_label = canvas.create_text(x, y, anchor="nw", text=sender_text, fill=text_color, font=sender_font)

    # Calcular la altura del mensaje con saltos de línea
    lines = message.split('\n')
    line_height = message_font.metrics('linespace')
    message_height = line_height * len(lines)

    # Añadir el mensaje
    text_items = []
    for i, line in enumerate(lines):
        line_y = y + (i * line_height)
        text = canvas.create_text(x + sender_font.measure(sender_text), line_y, anchor="nw", text=line, fill=text_color,
                                  font=message_font)
        text_items.append(text)

    # Ajustar la altura del rectángulo en función de la altura del mensaje
    rect_height = message_height + 10  # Reducir el padding si es necesario
    rect = canvas.create_rectangle(x - 5, y - 5, x + message_font.measure(message) + 30, y + rect_height,
                                   fill=fill_color, outline="")

    messages.append((rect, sender_label, *text_items))
    canvas.tag_raise(sender_label)  # Asegurarse de que el remitente esté por encima del rectángulo
    for text_item in text_items:
        canvas.tag_raise(text_item)  # Asegurarse de que el texto esté por encima del rectángulo

    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(1.0)  # Scroll hasta el final


# Configuración de la ventana principal
root = tk.Tk()
root.title("Chatbot")
root.geometry("500x600")
root.resizable(False, False)

# Configuración del canvas para mostrar la conversación
canvas_frame = tk.Frame(root)
canvas_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
canvas = tk.Canvas(canvas_frame, bg="#444444")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(canvas_frame, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.config(yscrollcommand=scrollbar.set)

# Almacenar los mensajes
messages = []

# Mensaje inicial del bot al iniciar el chatbot
display_message(mensaje_bienvenida, "bot")

# Campo de entrada de texto para el usuario
user_input = tk.StringVar()
entry_box = tk.Entry(root, textvariable=user_input, font=("Arial", 12))
entry_box.pack(padx=10, pady=10, fill=tk.X)
entry_box.bind("<Return>", send_message)

# Botón de enviar
send_button = tk.Button(root, text="Enviar", command=send_message, font=("Arial", 12))
send_button.pack(padx=10, pady=10)

# Estilizando los widgets
root.configure(bg="#333333")
entry_box.configure(bg="#555555", fg="#FFFFFF", insertbackground="#FFFFFF")
send_button.configure(bg="#666666", fg="#FFFFFF", activebackground="#777777", activeforeground="#FFFFFF")

root.mainloop()
