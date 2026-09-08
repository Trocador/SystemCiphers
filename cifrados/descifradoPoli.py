ALFABETO = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
texto_cifrado = input("Ingrese el texto cifrado con espacion entre pares (ej. 23 34 31 11): ")
pares = texto_cifrado.split()
resultado = []

for par in pares:
    if len(par) == 2 and par.isdigit():
        fila = int(par[0])
        columna = int(par[1])
        if 1 <= fila <= 5 and 1 <= columna <= 5:
            posicion = (fila - 1) * 5 + (columna - 1)
            letra = ALFABETO[posicion]
            resultado.append(letra)
        else:
            print(f"Advertencia: El par '{par}' tiene coordenadas fuera del rango 1-5.")
    else:
        print(f"Advertencia: '{par}' no es un par válido de 2 números.")

texto_descifrado = "".join(resultado)
print(f"Texto descifrado: {texto_descifrado}")