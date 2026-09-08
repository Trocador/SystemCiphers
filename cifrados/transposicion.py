import math

# --- TRANSPOSICIÓN POR GRUPOS ---
def cifrar_grupos(texto: str, clave: list) -> str:
    clave_base0 = [p - 1 for p in clave]
    tamano = len(clave_base0)
    
    while len(texto) % tamano != 0:
        texto += "X"
        
    resultado = ""
    for i in range(0, len(texto), tamano):
        bloque = texto[i:i+tamano]
        bloque_cifrado = "".join(bloque[p] for p in clave_base0)
        resultado += bloque_cifrado
    return resultado

def descifrar_grupos(texto_cifrado: str, clave: list) -> str:
    clave_base0 = [p - 1 for p in clave]
    tamano = len(clave_base0)
    
    clave_inversa = [0] * tamano
    for posicion_nueva, posicion_original in enumerate(clave_base0):
        clave_inversa[posicion_original] = posicion_nueva
        
    resultado = ""
    for i in range(0, len(texto_cifrado), tamano):
        bloque = texto_cifrado[i:i+tamano]
        bloque_descifrado = "".join(bloque[p] for p in clave_inversa)
        resultado += bloque_descifrado
    return resultado.rstrip("X")

# --- TRANSPOSICIÓN SERIAL ---
def cifrar_serial(texto: str) -> str:
    return texto[0::2] + texto[1::2]

def descifrar_serial(texto_cifrado: str) -> str:
    mitad = (len(texto_cifrado) + 1) // 2
    serie_par = texto_cifrado[:mitad]
    serie_impar = texto_cifrado[mitad:]
    resultado = []
    for i in range(len(serie_par)):
        resultado.append(serie_par[i])
        if i < len(serie_impar):
            resultado.append(serie_impar[i])
    return "".join(resultado)

# --- TRANSPOSICIÓN POR COLUMNAS ---
def cifrar_columnas(texto: str, clave: str) -> str:
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

def descifrar_columnas(texto_cifrado: str, clave: str) -> str:
    num_columnas = len(clave)
    num_filas = len(texto_cifrado) // num_columnas
    indices_ordenados = sorted(range(len(clave)), key=lambda k: clave[k])
    matriz = [[""] * num_columnas for _ in range(num_filas)]
    idx_texto = 0
    for col in indices_ordenados:
        for fila in range(num_filas):
            matriz[fila][col] = texto_cifrado[idx_texto]
            idx_texto += 1
    return "".join("".join(fila) for fila in matriz).strip()