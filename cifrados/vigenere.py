def cifrado_vigenere(texto: str, clave: str, cifrar: bool = True) -> tuple[str, str]:
    """
    Aplica Vigenère y retorna (resultado, esquema_visual).
    """
    clave = clave.upper()
    resultado = ""
    esquema = "--- ALINEACIÓN DE TEXTO Y CLAVE ---\n"
    
    # Preparar el texto alineado con la clave
    texto_limpio = "".join([c.upper() for c in texto if c.isalpha()])
    clave_repetida = ""
    j = 0

    for c in texto:
        if c.isalpha():
            char_clave = clave[j % len(clave)]
            clave_repetida += char_clave
            
            base = ord('A') if c.isupper() else ord('a')
            k = ord(char_clave) - 65
            desplazamiento = k if cifrar else -k
            
            nuevo_char = chr((ord(c) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
            j += 1
        else:
            clave_repetida += " "
            resultado += c

    # Construir el esquema visual
    esquema += f"Texto:  {texto}\n"
    esquema += f"Clave:  {clave_repetida}\n"
    esquema += f"Salida: {resultado}\n\n"
    esquema += "--- TABLA DE VIGENÈRE (Muestras de cruce) ---\n"
    esquema += " Letra Texto + Letra Clave = Letra Resultado\n"
    esquema += " -------------------------------------------\n"

    j = 0
    for c in texto:
        if c.isalpha():
            char_clave = clave[j % len(clave)]
            res_char = resultado[len(esquema.splitlines()) - 6] # Rastrear carácter
            esquema += f"   '{c.upper()}'     +    '{char_clave}'       =     '{cifrado_vigenere_char(c, char_clave, cifrar)}'\n"
            j += 1

    return resultado, esquema


def cifrado_vigenere_char(char_texto: str, char_clave: str, cifrar: bool) -> str:
    """Calcula la letra resultante individual."""
    base = ord('A') if char_texto.isupper() else ord('a')
    k = ord(char_clave) - 65
    desplazamiento = k if cifrar else -k
    return chr((ord(char_texto) - base + desplazamiento) % 26 + base)


def descifrado_vigenere(texto: str, clave: str) -> tuple[str, str]:
    """Descifra Vigenère devolviendo resultado y esquema."""
    return cifrado_vigenere(texto, clave, cifrar=False)