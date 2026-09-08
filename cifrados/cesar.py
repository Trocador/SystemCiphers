def cifrado_cesar(texto: str, n_posiciones: int = 3) -> str:
    """Cifra un texto desplazando las letras 'n_posiciones' (Por defecto 3)."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nuevo_char = chr((ord(char) - base + n_posiciones) % 26 + base)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado


def descifrado_cesar(texto: str, n_posiciones: int = 3) -> str:
    """Descifra un texto aplicando el desplazamiento inverso '-n_posiciones'."""
    return cifrado_cesar(texto, -n_posiciones)