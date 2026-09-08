def cifrado_adicion(texto: str, clave: int) -> str:
    """Cifra el texto sumando el valor de la clave a cada letra (Aritmética Modular)."""
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # C = (P + K) mod 26
            nuevo_char = chr((ord(char) - base + clave) % 26 + base)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado


def descifrado_adicion(texto: str, clave: int) -> str:
    """Descifra aplicando la resta de la clave: P = (C - K) mod 26."""
    return cifrado_adicion(texto, -clave)