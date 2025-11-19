#cbtis 89
# 3°b programacion matutino
# Escobedo Escobar Kevin ALejandro

import tkinter as tk
from tkinter import Toplevel

#crear la ventana principal
ventana_principal = tk.Tk ()
ventana_principal.title("Ventana principal")
ventana_principal.geometry("300x200")

# funcion para abrir una ventana hija
def abrir_ventana_hija():
    ventana_hija = Toplevel(ventana_principal)
    ventana_hija.title("ventana hija")
    ventana_hija.geometru("250x150")

    etiqueta = tk.Label(ventana_hija, text="Esta es una ventana hija", front=("Arial", 12))
    etiqueta.pack(pady=10)

    boton_cerrar =tk.Button(ventana_hija, text= "cerrar", comand=ventana_hija.destroy)
    boton_cerrar.pack(pady=10)

#boton en la ventana principal oara abrir la ventana hija 
boton_abrir = tk.Button(ventana_principal, text="abrir ventana hija ", command= abrir_ventana_hija)
boton_abrir.pack (pady=20)

#iniciar el loop principal
ventana_principal.mainloop