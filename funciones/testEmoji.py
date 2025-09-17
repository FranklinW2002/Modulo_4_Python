import emoji
cantidadFrase = int(input("Cuantas frases desea ingresar: "))
for i in range(cantidadFrase):
    frase = input("Ingrese su frase: ")
    emoji.encontarPalabra(frase)
    emoji.agregarFrase(frase)