import math

# --- TRANSPOSICIÓN POR GRUPOS ---
def cifrar_grupos(texto: str, clave: list):
    clave_base0 = [p - 1 for p in clave]
    tamano = len(clave_base0)
    
    # Relleno con X
    texto_procesado = texto
    while len(texto_procesado) % tamano != 0:
        texto_procesado += "X"
        
    resultado = ""
    esquema_bloques = []
    
    for i in range(0, len(texto_procesado), tamano):
        bloque = texto_procesado[i:i+tamano]
        bloque_cifrado = "".join(bloque[p] for p in clave_base0)
        resultado += bloque_cifrado
        esquema_bloques.append(f"Bloque {i//tamano + 1}: [{bloque}] ➔ Permutación {clave}: [{bloque_cifrado}]")
    
    guia_visual = "\n".join(esquema_bloques)
    return resultado, guia_visual

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
def cifrar_serial(texto: str):
    pares = texto[0::2]
    impares = texto[1::2]
    resultado = pares + impares
    
    guia_visual = (
        f"Posiciones Pares   (0, 2, 4...): {pares}\n"
        f"Posiciones Impares (1, 3, 5...): {impares}\n"
        f"Union Final (Pares + Impares)  : {resultado}"
    )
    return resultado, guia_visual

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
def cifrar_columnas(texto: str, clave: str):
    num_columnas = len(clave)
    num_filas = math.ceil(len(texto) / num_columnas)
    texto_relleno = texto.ljust(num_columnas * num_filas, " ")
    matriz = [texto_relleno[i:i+num_columnas] for i in range(0, len(texto_relleno), num_columnas)]
    
    # Obtener el orden de lectura según el orden alfabético de la clave
    indices_ordenados = sorted(range(len(clave)), key=lambda k: clave[k])
    
    resultado = ""
    for col in indices_ordenados:
        for fila in matriz:
            resultado += fila[col]
            
    # Formatear la matriz en texto tipo tabla
    linea_header = "  ".join(list(clave.upper()))
    linea_indices = "  ".join(str(i+1) for i in range(num_columnas))
    separador = "-" * (num_columnas * 3)
    
    filas_texto = []
    for fila in matriz:
        filas_texto.append("  ".join(fila))
        
    orden_lectura = " -> ".join([f"Col '{clave[i]}'" for i in indices_ordenados])
    
    guia_visual = (
        f"CLAVE:   {linea_header}\n"
        f"ORDEN:   {linea_indices}\n"
        f"{separador}\n" +
        "\n".join(filas_texto) +
        f"\n{separador}\n"
        f"Secuencia de lectura por columnas: {orden_lectura}"
    )
    
    return resultado, guia_visual

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