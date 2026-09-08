import tkinter as tk
from tkinter import messagebox


# ==============================
# CREAR ALFABETO CON CLAVE
# ==============================

def crear_alfabeto_clave(clave):

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nuevo = ""

    # Colocar letras de la clave sin repetir
    for letra in clave.upper():

        if letra in alfabeto and letra not in nuevo:
            nuevo += letra

    # Completar con las letras faltantes
    for letra in alfabeto:

        if letra not in nuevo:
            nuevo += letra

    return nuevo


# ==============================
# CIFRADO CÉSAR CON CLAVE
# ==============================

def cesar_con_clave(texto, clave):

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    alfabeto_clave = crear_alfabeto_clave(clave)

    resultado = ""

    for letra in texto.upper():

        if letra in alfabeto:

            posicion = alfabeto.index(letra)

            resultado += alfabeto_clave[posicion]

        else:

            resultado += letra

    return resultado


# ==============================
# FUNCIÓN DEL BOTÓN CIFRAR
# ==============================

def cifrar():

    clave = entrada_clave.get()
    texto = entrada_texto.get()

    if clave == "" or texto == "":

        messagebox.showwarning(
            "Aviso",
            "Complete los datos"
        )

        return

    resultado = cesar_con_clave(
        texto,
        clave
    )

    salida.config(
        text="Texto cifrado: " + resultado
    )


# ==============================
# INTERFAZ
# ==============================

ventana = tk.Tk()

ventana.title("César con Clave")

ventana.geometry("500x400")

ventana.configure(
    bg="#F1F5F8"
)


# TÍTULO

tk.Label(
    ventana,
    text="César con Clave",
    font=("Arial", 22, "bold"),
    bg="#F1F5F8",
    fg="#0A416D"
).pack(
    pady=20
)


# CLAVE

tk.Label(
    ventana,
    text="Clave:",
    font=("Arial", 13, "bold"),
    bg="#F1F5F8"
).pack()


entrada_clave = tk.Entry(
    ventana,
    font=("Arial", 14),
    width=30
)

entrada_clave.pack(
    pady=10
)


# TEXTO PLANO

tk.Label(
    ventana,
    text="Texto plano:",
    font=("Arial", 13, "bold"),
    bg="#F1F5F8"
).pack()


entrada_texto = tk.Entry(
    ventana,
    font=("Arial", 14),
    width=30
)

entrada_texto.pack(
    pady=10
)


# BOTÓN CIFRAR

tk.Button(
    ventana,
    text="CIFRAR",
    command=cifrar,
    font=("Arial", 13, "bold"),
    bg="#1677E8",
    fg="white",
    width=15
).pack(
    pady=20
)


# RESULTADO

salida = tk.Label(
    ventana,
    text="Texto cifrado:",
    font=("Arial", 15, "bold"),
    bg="#F1F5F8",
    fg="#0A416D"
)

salida.pack(
    pady=10
)


# ==============================
# EJECUTAR PROGRAMA
# ==============================

ventana.mainloop()