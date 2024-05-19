import tkinter as tk
from PIL import Image, ImageTk

# Función para cambiar el color de fondo
def cambiar_color(color):
    ventana.config(bg=color)

ventana = tk.Tk()
ventana.geometry("1920x1080")
ventana.config(bg="#CCA9DD", padx=100, pady=100)

frame = tk.Frame(ventana)
frame.pack()

texto = tk.Label(frame, fg="red", text="¡Hola clase!")
texto.grid(row=0, column=0, columnspan=2)

# Añadir cuadro de texto para que el usuario escriba
entrada = tk.Entry(frame)
entrada.grid(row=1, column=0, columnspan=2, pady=10)

# Cargar la imagen y convertirla a un formato compatible con Tkinter
imagen = Image.open("programacion.png")
imagen = ImageTk.PhotoImage(imagen)

# Crear una etiqueta para mostrar la imagen dentro del frame
label_imagen = tk.Label(frame, image=imagen)
label_imagen.image = imagen  # Mantener una referencia para evitar que la imagen se elimine
label_imagen.grid(row=2, column=0, columnspan=2)

# Botones para cambiar el color de fondo
boton_amarillo = tk.Button(frame, text="Fondo Amarillo", command=lambda: cambiar_color("yellow"))
boton_amarillo.grid(row=3, column=0, padx=10, pady=10)

boton_azul = tk.Button(frame, text="Fondo Azul", command=lambda: cambiar_color("blue"))
boton_azul.grid(row=3, column=1, padx=10, pady=10)

ventana.mainloop()
