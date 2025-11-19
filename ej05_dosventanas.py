#cbtis 89
# 3°b programacion matutino
# Escobedo Escobar Kevin ALejandro
import tkinter as tk
from tkinter import Toplevel

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Kevin Alejandro Escobedo Escobar")
ventana_principal.geometry("300x200")

tk.Label (ventana_principal, text="Kevin Alejandro Escobedo Escobar", font=('Arial', 12)).pack()

# Función para abrir una ventana hija
def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("Ventana de alejandro")
    ventana_hija.geometry("250x150")

    

    etiqueta = tk.Label(ventana_hija, text='PROGRAMANDO CON PYTHON', font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_hija, text="Cerrar ventana", command=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

# Botón en la ventana principal para abrir la ventana hija

boton_abrir = tk.Button(ventana_principal, text="Ventana", command=abrir_ventana_hija)
boton_abrir.pack(pady=20)

# Iniciar el loop principal
ventana_principal.mainloop()