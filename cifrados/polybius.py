# Definición de la matriz 5x5 tradicional (I/J comparten la misma celda)
TABLA_POLYBIUS = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],  # 'J' se mapea a 'I' (24)
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

def cifrado_polybius(texto: str) -> str:
    """Convierte cada letra en sus coordenadas de fila y columna (1-5)."""
    resultado = []
    texto_limpio = texto.upper().replace('J', 'I')
    
    for char in texto_limpio:
        if char.isalpha():
            encontrado = False
            for f in range(5):
                for c in range(5):
                    if TABLA_POLYBIUS[f][c] == char:
                        # Coordenadas base 1 (FilaColumna)
                        resultado.append(f"{f + 1}{c + 1}")
                        encontrado = True
                        break
                if encontrado:
                    break
        else:
            resultado.append(char)
            
    return " ".join(resultado)


def descifrado_polybius(texto: str) -> str:
    """Convierte pares de coordenadas de vuelta a texto."""
    elementos = texto.strip().split()
    resultado = []
    
    for item in elementos:
        if len(item) == 2 and item.isdigit():
            f = int(item[0]) - 1
            c = int(item[1]) - 1
            if 0 <= f < 5 and 0 <= c < 5:
                resultado.append(TABLA_POLYBIUS[f][c])
            else:
                resultado.append(item)
        else:
            resultado.append(item)
            
    return "".join(resultado)