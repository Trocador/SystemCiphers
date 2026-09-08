import tkinter as tk
from tkinter import messagebox


# ---------------- CIFRADO POR ADICIÓN ----------------

def cifrado_adicion(texto, clave):

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resultado = []

    texto = texto.upper()
    clave = clave.upper()

    for i, letra in enumerate(texto):

        if letra in alfabeto:

            numero_texto = alfabeto.index(letra)

            numero_clave = alfabeto.index(
                clave[i % len(clave)]
            )

            suma = numero_texto + numero_clave

            resultado.append(str(suma))

        else:
            resultado.append(letra)

    return " ".join(resultado)



# ---------------- BOTÓN CIFRAR ----------------

def cifrar():

    clave = entrada_clave.get()
    texto = entrada_texto.get()

    if clave == "" or texto == "":
        messagebox.showwarning(
            "Aviso",
            "Ingrese la clave y el texto plano"
        )
        return


    resultado = cifrado_adicion(
        texto,
        clave
    )


    salida.config(
        text=resultado
    )



# ---------------- VENTANA PRINCIPAL ----------------

ventana = tk.Tk()

ventana.title("Sistema de Cifrados")

ventana.geometry("650x520")

ventana.configure(
    bg="#eef3f8"
)



# ---------------- ENCABEZADO ----------------

header = tk.Frame(
    ventana,
    bg="#123b63",
    height=100
)


# ---------------- TARJETA ----------------

tarjeta = tk.Frame(
    ventana,
    bg="white",
    width=500,
    height=330
)

tarjeta.pack(
    pady=35
)



titulo2 = tk.Label(
    tarjeta,
    text="Cifrado por Adición",
    font=("Arial",18,"bold"),
    fg="#123b63",
    bg="white"
)

titulo2.pack(
    pady=15
)



descripcion = tk.Label(
    tarjeta,
    text="Convierte letras a valores numéricos sumando la clave",
    font=("Arial",11),
    fg="#555",
    bg="white"
)

descripcion.pack()



# ---------------- CAMPOS ----------------


tk.Label(
    tarjeta,
    text="Clave:",
    font=("Arial",12,"bold"),
    bg="white"
).pack(
    pady=(15,5)
)


entrada_clave = tk.Entry(
    tarjeta,
    width=40,
    font=("Arial",12),
    relief="solid"
)

entrada_clave.pack()



tk.Label(
    tarjeta,
    text="Texto plano:",
    font=("Arial",12,"bold"),
    bg="white"
).pack(
    pady=(15,5)
)


entrada_texto = tk.Entry(
    tarjeta,
    width=40,
    font=("Arial",12),
    relief="solid"
)

entrada_texto.pack()



# ---------------- BOTÓN ----------------


boton = tk.Button(
    tarjeta,
    text="🔒 CIFRAR",
    width=20,
    height=2,
    bg="#1769d2",
    fg="white",
    font=("Arial",12,"bold"),
    relief="flat",
    cursor="hand2",
    command=cifrar
)


boton.pack(
    pady=25
)



# ---------------- RESULTADO ----------------


tk.Label(
    tarjeta,
    text="Texto cifrado:",
    font=("Arial",12,"bold"),
    bg="white"
).pack()



salida = tk.Label(
    tarjeta,
    text="Esperando resultado...",
    font=("Arial",13),
    fg="#1769d2",
    bg="white",
    wraplength=450
)


salida.pack(
    pady=10
)


ventana.mainloop()