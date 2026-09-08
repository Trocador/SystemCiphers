def cifrar_rail_fence(texto, num_railes):
    if num_railes <= 1:
        return texto.replace(" ", "").upper()

    texto = texto.upper().replace(" ", "")

    railes = [[] for _ in range(num_railes)]

    rail_actual = 0
    direccion = 1  # 1 significa bajar, -1 significa subir

    for caracter in texto:
        railes[rail_actual].append(caracter)

        if rail_actual == 0:
            direccion = 1
        elif rail_actual == num_railes - 1:
            direccion = -1

        rail_actual += direccion

    cifrado_final = "".join(["".join(rail) for rail in railes])
    return cifrado_final

mensaje = (input("Ingrese el texto a cifrar: "))
railes = 4
resultado = cifrar_rail_fence(mensaje, railes)
print(f"Texto cifrado: {resultado}")