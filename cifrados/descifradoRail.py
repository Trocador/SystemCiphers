def descifrar_rail_fence(texto_cifrado, num_railes):
    if num_railes <= 1 or not texto_cifrado:
        return texto_cifrado

    n = len(texto_cifrado)
    matriz = [[None] * n for _ in range(num_railes)]

    rail_actual = 0
    direccion = 1

    for col in range(n):
        matriz[rail_actual][col] = "*"

        if rail_actual == 0:
            direccion = 1
        elif rail_actual == num_railes - 1:
            direccion = -1

        rail_actual += direccion

    index_texto = 0
    for r in range(num_railes):
        for c in range(n):
            if matriz[r][c] == "*" and index_texto < n:
                matriz[r][c] = texto_cifrado[index_texto]
                index_texto += 1

    texto_descifrado = []
    rail_actual = 0
    direccion = 1

    for col in range(n):
        texto_descifrado.append(matriz[rail_actual][col])

        if rail_actual == 0:
            direccion = 1
        elif rail_actual == num_railes - 1:
            direccion = -1

        rail_actual += direccion

    return "".join(texto_descifrado)

cifrado = input("Ingrese el texto cifrado: ")
railes = 4
original = descifrar_rail_fence(cifrado, railes)
print(f"Texto descifrado: {original}")