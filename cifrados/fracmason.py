# Mapeo de letras al alfabeto gráfico del cifrado Fracmasón (Pigpen)
MAPA_FRACMASON = {
    'A': '└┘', 'B': '└┴┘', 'C': '└─┘',
    'D': '┌┐', 'E': '┌┬┐', 'F': '┌─┐',
    'G': '╘╛', 'H': '╘╧╛', 'I': '╘═╛',
    'J': '└┘•', 'K': '└┴┘•', 'L': '└─┘•',
    'M': '┌┐•', 'N': '┌┬┐•', 'O': '┌─┐•',
    'P': '╘╛•', 'Q': '╘╧╛•', 'R': '╘═╛•',
    'S': '><', 'T': '>•<', 'U': 'V',
    'V': 'V•', 'W': 'X', 'X': 'X•',
    'Y': '∧',  'Z': '∧•'
}

# Diccionario invertido para el descifrado
MAPA_INVERSO = {v: k for k, v in MAPA_FRACMASON.items()}


def cifrado_fracmason(texto: str) -> str:
    """Convierte el texto a sus símbolos geométricos Pigpen/Fracmasón."""
    resultado = []
    for char in texto.upper():
        if char in MAPA_FRACMASON:
            resultado.append(MAPA_FRACMASON[char])
        else:
            resultado.append(char)
    return " ".join(resultado)


def descifrado_fracmason(texto: str) -> str:
    """Convierte la cadena de símbolos Pigpen de vuelta a texto claro."""
    simbolos = texto.strip().split()
    resultado = []
    for sim in simbolos:
        if sim in MAPA_INVERSO:
            resultado.append(MAPA_INVERSO[sim])
        else:
            resultado.append(sim)
    return "".join(resultado)