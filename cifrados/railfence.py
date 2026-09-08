def cifrado_railfence(texto: str, rieles: int):
    if rieles <= 1 or rieles >= len(texto):
        return texto, texto

    matriz = [['.' for _ in range(len(texto))] for _ in range(rieles)]
    fila_actual = 0
    direccion_abajo = False

    for i, char in enumerate(texto):
        if fila_actual == 0 or fila_actual == rieles - 1:
            direccion_abajo = not direccion_abajo
        
        matriz[fila_actual][i] = char if char != ' ' else '␣'
        fila_actual += 1 if direccion_abajo else -1

    # Construir el texto cifrado
    resultado = []
    for f in range(rieles):
        for c in range(len(texto)):
            if matriz[f][c] != '.':
                resultado.append(matriz[f][c] if matriz[f][c] != '␣' else ' ')

    # Construir la representación gráfica en zigzag (String)
    representacion_grafica = "\n".join([" ".join(fila) for fila in matriz])

    return "".join(resultado), representacion_grafica


def descifrado_railfence(texto: str, rieles: int) -> str:
    """Descifra reconstruyendo la matriz en zigzag a partir del texto transpuesto."""
    if rieles <= 1 or rieles >= len(texto):
        return texto

    # Matriz para marcar las posiciones del zigzag
    matriz = [['' for _ in range(len(texto))] for _ in range(rieles)]
    
    fila_actual = 0
    direccion_abajo = False

    # Marcar con '*' las posiciones que ocupará el texto
    for i in range(len(texto)):
        if fila_actual == 0 or fila_actual == rieles - 1:
            direccion_abajo = not direccion_abajo
        matriz[fila_actual][i] = '*'
        fila_actual += 1 if direccion_abajo else -1

    # Rellenar la matriz con los caracteres del texto cifrado
    indice = 0
    for f in range(rieles):
        for c in range(len(texto)):
            if matriz[f][c] == '*' and indice < len(texto):
                matriz[f][c] = texto[indice]
                indice += 1

    # Leer en zigzag para recuperar el mensaje original
    resultado = []
    fila_actual = 0
    direccion_abajo = False

    for i in range(len(texto)):
        if fila_actual == 0 or fila_actual == rieles - 1:
            direccion_abajo = not direccion_abajo
        
        if matriz[fila_actual][i] != '':
            resultado.append(matriz[fila_actual][i])
        fila_actual += 1 if direccion_abajo else -1

    return "".join(resultado)