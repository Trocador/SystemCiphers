import math
import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# 1. ALGORITMOS DE CRIPTOGRAFÍA
# ==========================================

def cifrar_grupos(texto, clave):
    tamano = len(clave)
    while len(texto) % tamano != 0:
        texto += " "
    resultado = ""
    for i in range(0, len(texto), tamano):
        bloque = texto[i:i+tamano]
        bloque_cifrado = "".join(bloque[p] for p in clave)
        resultado += bloque_cifrado
    return resultado

def descifrar_grupos(texto_cifrado, clave):
    tamano = len(clave)
    clave_inversa = [0] * tamano
    for posicion_nueva, posicion_original in enumerate(clave):
        clave_inversa[posicion_original] = posicion_nueva
    resultado = ""
    for i in range(0, len(texto_cifrado), tamano):
        bloque = texto_cifrado[i:i+tamano]
        bloque_descifrado = "".join(bloque[p] for p in clave_inversa)
        resultado += bloque_descifrado
    return resultado.strip()

def cifrar_serial(texto):
    serie_par = texto[0::2]
    serie_impar = texto[1::2]
    return serie_par + serie_impar

def descifrar_serial(texto_cifrado):
    mitad = (len(texto_cifrado) + 1) // 2
    serie_par = texto_cifrado[:mitad]
    serie_impar = texto_cifrado[mitad:]
    resultado = []
    for i in range(len(serie_par)):
        resultado.append(serie_par[i])
        if i < len(serie_impar):
            resultado.append(serie_impar[i])
    return "".join(resultado)

def cifrar_columnas(texto, clave):
    num_columnas = len(clave)
    num_filas = math.ceil(len(texto) / num_columnas)
    texto_relleno = texto.ljust(num_columnas * num_filas, " ")
    matriz = [texto_relleno[i:i+num_columnas] for i in range(0, len(texto_relleno), num_columnas)]
    indices_ordenados = sorted(range(len(clave)), key=lambda k: clave[k])
    resultado = ""
    for col in indices_ordenados:
        for fila in matriz:
            resultado += fila[col]
    return resultado

def descifrar_columnas(texto_cifrado, clave):
    num_columnas = len(clave)
    num_filas = len(texto_cifrado) // num_columnas
    indices_ordenados = sorted(range(len(clave)), key=lambda k: clave[k])
    matriz = [[""] * num_columnas for _ in range(num_filas)]
    idx_texto = 0
    for col in indices_ordenados:
        for fila in range(num_filas):
            matriz[fila][col] = texto_cifrado[idx_texto]
            idx_texto += 1
    resultado = "".join("".join(fila) for fila in matriz)
    return resultado.strip()

# ==========================================
# 2. LÓGICA DE CONTROL
# ==========================================

def procesar():
    metodo = combo_metodo.get()
    accion = var_accion.get()
    texto = entry_texto.get()
    clave = entry_clave.get()

    if not texto:
        messagebox.showwarning("Atención", "Por favor, ingresa un texto.")
        return

    resultado = ""

    try:
        if metodo == "Transposición en Grupos":
            if not clave:
                messagebox.showwarning("Atención", "Este método requiere una clave numérica (ej. 1,0,3,2).")
                return
            clave_lista = [int(x) for x in clave.split(",")]
            if accion == "Cifrar":
                resultado = cifrar_grupos(texto, clave_lista)
            else:
                resultado = descifrar_grupos(texto, clave_lista)

        elif metodo == "Transposición Serial":
            if accion == "Cifrar":
                resultado = cifrar_serial(texto)
            else:
                resultado = descifrar_serial(texto)

        elif metodo == "Transposición por Columnas":
            if not clave:
                messagebox.showwarning("Atención", "Este método requiere una palabra clave.")
                return
            if accion == "Cifrar":
                resultado = cifrar_columnas(texto, clave)
            else:
                resultado = descifrar_columnas(texto, clave)

        entry_resultado.config(state="normal")
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        entry_resultado.config(state="readonly")

    except Exception as e:
        messagebox.showerror("Error", f"Verifica el formato de tus datos.\n\nDetalles: {e}")

# ==========================================
# 3. INTERFAZ GRÁFICA DE ALTO IMPACTO (CYBERPUNK)
# ==========================================

COLOR_FONDO_1 = "#0d1117"     # Negro profundo espacial
COLOR_TARJETA = "#161b22"     # Gris oscuro metálico
TEXTO_NEON = "#00f0ff"        # Cian Neón eléctrico
TEXTO_SECUNDARIO = "#8b949e"  # Gris claro texturizado
BOTON_NORMAL = "#ff007f"      # Fucsia Neón muy llamativo
BOTON_HOVER = "#e60072"       # Fucsia más oscuro para el efecto
INPUT_BG = "#21262d"          # Fondo oscuro para las cajas

ventana = tk.Tk()
ventana.title("Sistema Criptográfico Avanzado")
ventana.geometry("540x580")
ventana.configure(bg=COLOR_FONDO_1)

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("TCombobox", fieldbackground=INPUT_BG, background=COLOR_TARJETA, foreground="white", bordercolor=TEXTO_NEON)

tk.Label(ventana, text="CRIPTOGRAFÍA DE TRANSPOSICIÓN", font=("Impact", 20), fg=TEXTO_NEON, bg=COLOR_FONDO_1).pack(pady=20)

panel_central = tk.Frame(ventana, bg=COLOR_TARJETA, bd=2, highlightbackground=TEXTO_NEON, relief="solid")
panel_central.pack(fill="both", expand=True, padx=30, pady=5)

tk.Label(panel_central, text="MÉTODO SELECCIONADO", font=("Segoe UI", 9, "bold"), fg=TEXTO_NEON, bg=COLOR_TARJETA).pack(pady=(15, 2))
combo_metodo = ttk.Combobox(panel_central, values=["Transposición en Grupos", "Transposición Serial", "Transposición por Columnas"], state="readonly", width=32, font=("Segoe UI", 10, "bold"))
combo_metodo.current(0)
combo_metodo.pack(pady=5)

var_accion = tk.StringVar(value="Cifrar")
marco_radios = tk.Frame(panel_central, bg=COLOR_TARJETA)
marco_radios.pack(pady=10)

rb_cifrar = tk.Radiobutton(marco_radios, text="CIFRAR MENSAJE", variable=var_accion, value="Cifrar", font=("Segoe UI", 9, "bold"), fg="white", bg=COLOR_TARJETA, activebackground=COLOR_TARJETA, activeforeground=TEXTO_NEON, selectcolor=COLOR_FONDO_1)
rb_cifrar.pack(side="left", padx=15)

rb_descifrar = tk.Radiobutton(marco_radios, text="DESCIFRAR MENSAJE", variable=var_accion, value="Descifrar", font=("Segoe UI", 9, "bold"), fg="white", bg=COLOR_TARJETA, activebackground=COLOR_TARJETA, activeforeground=TEXTO_NEON, selectcolor=COLOR_FONDO_1)
rb_descifrar.pack(side="left", padx=15)

tk.Label(panel_central, text="MENSAJE DE ENTRADA:", font=("Segoe UI", 9, "bold"), fg=TEXTO_SECUNDARIO, bg=COLOR_TARJETA).pack(pady=(10, 2))
entry_texto = tk.Entry(panel_central, width=42, font=("Consolas", 11), bg=INPUT_BG, fg="white", bd=1, relief="solid", highlightcolor=TEXTO_NEON, insertbackground="white")
entry_texto.pack(pady=2)

tk.Label(panel_central, text="CLAVE REQUERIDA:", font=("Segoe UI", 9, "bold"), fg=TEXTO_SECUNDARIO, bg=COLOR_TARJETA).pack(pady=(10, 2))
entry_clave = tk.Entry(panel_central, width=42, font=("Consolas", 11), bg=INPUT_BG, fg="white", bd=1, relief="solid", highlightcolor=TEXTO_NEON, insertbackground="white")
entry_clave.pack(pady=2)

def al_entrar(e): btn_procesar.config(bg=BOTON_HOVER)
def al_salir(e): btn_procesar.config(bg=BOTON_NORMAL)

btn_procesar = tk.Button(panel_central, text="EJECUTAR ALGORITMO", command=procesar, bg=BOTON_NORMAL, fg="white", font=("Arial Black", 11), bd=0, cursor="hand2", padx=20, pady=8, activebackground=BOTON_HOVER, activeforeground="white")
btn_procesar.pack(pady=20)

btn_procesar.bind("<Enter>", al_entrar)
btn_procesar.bind("<Leave>", al_salir)

tk.Label(panel_central, text="RESULTADO DEL PROCESO", font=("Segoe UI", 10, "bold"), fg=TEXTO_NEON, bg=COLOR_TARJETA).pack(pady=(5, 2))
entry_resultado = tk.Entry(panel_central, width=38, font=("Consolas", 13, "bold"), bg=COLOR_FONDO_1, fg="#00ff66", bd=1, relief="solid", justify="center")
entry_resultado.config(state="readonly")
entry_resultado.pack(pady=(2, 20))

ventana.mainloop()
