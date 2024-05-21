import tkinter as tk
from tkinter import ttk

def limpiar_elementos():
    entrada_contra.delete(0, tk.END)
    entrada_usuario.delete(0, tk.END)
    combobox.delete(0, tk.END)

def obtener_texto():
    texto_usuario = entrada_usuario.get()
    texto_contra = entrada_contra.get()
    seleccion_rol = combobox.get()

    vacio = True

    mensaje = ""
    if not texto_usuario:
        mensaje += "- Usuario está vacío.\n"
    if not texto_contra:
        mensaje += "- Contraseña está vacía.\n"
    if not seleccion_rol:
        mensaje += "- Rol no seleccionado.\n"
    
    if not mensaje:
        mensaje = f"Sesión iniciada\nNombre: {texto_usuario}\nRol: {seleccion_rol}"
        vacio = False
    
    ventana_emergente(mensaje, vacio)

def ventana_emergente(mensaje, vacio):
    emergente = tk.Tk()
    emergente.geometry("300x170")
    emergente.config(bg="#c0c0c0")
    
    etiqueta_mensaje = tk.Label(emergente, text=mensaje, bg="#c0c0c0", font=("Times New Roman", 12))
    etiqueta_mensaje.pack(pady=20)
    
    boton_cerrar = tk.Button(emergente, text="Cerrar", command=emergente.destroy)
    boton_cerrar.pack(pady=10)
    if (vacio == False):
        ventana.destroy()





ventana = tk.Tk()
ventana.geometry("350x250")
ventana.config(bg = "#c0c0c0")

Titulo = tk.Label(ventana, text="IES CANARIAS", bg = "#c0c0c0", font = ("Times New Roman",24, "bold"), pady=20)
Titulo.pack()

frame = tk.Frame(ventana, bg = "#c0c0c0")
frame.pack()

usuario = tk.Label(frame, text="Usuario:", bg = "#c0c0c0", font=("Times New Roman", 12))
usuario.grid(row=0, column=0)

entrada_usuario = tk.Entry(frame)
entrada_usuario.grid(row=0, column=1, pady=10, padx = 40)

contra = tk.Label(frame, text="Contraseña:", bg = "#c0c0c0", font=("Times New Roman", 12))
contra.grid(row=1, column=0, padx=(22,0))

entrada_contra = tk.Entry(frame)
entrada_contra.grid(row=1, column=1, pady=10, padx = 40)

rol = tk.Label(frame, text="Rol:", bg = "#c0c0c0", font=("Times New Roman", 12) )
rol.grid(row=3, column=0, padx=(0,30))

opciones = ["Administrador", "Empleado", "Invitado"]
combobox = ttk.Combobox(frame, values=opciones, state = "readonly", font=("Times New Roman", 12))
combobox.grid(row=3, column=1, pady=10, padx=(53,0))


boton_limpiar = tk.Button(frame, text="Reset", command=limpiar_elementos, font=("Times New Roman", 12))
boton_limpiar.grid(row=4, column=1, padx=(0,150))

boton_login = tk.Button(frame, text="Login", command=obtener_texto, font=("Times New Roman", 12))
boton_login.grid(row=4, column=0, pady=10)

ventana.mainloop()
