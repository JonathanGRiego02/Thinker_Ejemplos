import tkinter as tk # Importamos la libreria

ventana = tk.Tk() # Creamos la ventana

ventana.geometry("1920x1080") # Cambiamos el tamaño

ventana.config(bg = "#CCA9DD", padx = 100, pady = 100) # Configuración de parámetros

texto = tk.Label(ventana, fg = "red", text="¡Hola clase!") # Texto de ejemplo

texto.pack()

ventana.mainloop() # Iniciamos la ventana 