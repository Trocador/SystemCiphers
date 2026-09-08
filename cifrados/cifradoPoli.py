ALFABETO = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
resultado = []

texto = input("Ingrese el texto a cifrar: ")

texto = texto.upper().replace("J", "I")

for caracter in texto:
    if caracter in ALFABETO:
        posicion = ALFABETO.index(caracter)
        fila = (posicion // 5) + 1
        columna = (posicion % 5) + 1
        resultado.append(f"{fila}{columna}")

cifrado_final = " ".join(resultado)

print(f"Texto cifrado: {cifrado_final}")