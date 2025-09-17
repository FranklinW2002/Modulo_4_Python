
print("Selecione ingresando un numero")
pais = int(input("ingrese el pais:\n1 Ecuador\n2 Colombia\n3 Peru\n "))

print("Selecione ingresando un numero")
zona = int(input("Seleccione la zona: \n1 Urbana\n2 Rural\n3 Perimetral\n"))

velocidad = int(input("Ingrese su velocidad en km:\n"))

if pais == 1:
    if zona == 1:
        if velocidad>50:
            print("Reduzca su velocidad maximo permitido 50 km/h")
        elif velocidad<10:
            print("Aumente su velocida minimo permitido 10 km/h")
        else:
            print("Su velocidad es correcta")
    if zona == 2:
        if velocidad>70:
            print("Reduzca su velocidad maximo permitido 70 km/h")
        elif velocidad<51:
            print("Aumente su velocida minimo permitido 51 km/h")
        else:
            print("Su velocidad es correcta")
    if zona == 3:
        if velocidad>90:
            print("Reduzca su velocidad maximo permitido 90 km/h")
        elif velocidad<71:
            print("Aumente su velocida minimo permitido 71 km/h")
        else:
            print("Su velocidad es correcta")
elif pais == 2:
    if zona == 1:
        if velocidad>30:
            print("Reduzca su velocidad maximo permitido 30 km/h")
        elif velocidad<10:
            print("Aumente su velocida minimo permitido 10 km/h")
        else:
            print("Su velocidad es correcta")
    if zona == 2:
        if velocidad>80:
            print("Reduzca su velocidad maximo permitido 80 km/h")
        elif velocidad<31:
            print("Aumente su velocida minimo permitido 31 km/h")
        else:
            print("Su velocidad es correcta")
    if zona == 3:
        if velocidad>100:
            print("Reduzca su velocidad maximo permitido 100 km/h")
        elif velocidad<81:
            print("Aumente su velocida minimo permitido 81 km/h")
        else:
            print("Su velocidad es correcta")
elif pais == 3:
    if zona == 1:
        if velocidad>40:
            print("Reduzca su velocidad maximo permitido 40 km/h")
        elif velocidad<10:
            print("Aumente su velocida minimo permitido 10 km/h")
        else:
            print("Su velocidad es correcta")
    if zona == 2:
        if velocidad>60:
            print("Reduzca su velocidad maximo permitido 60 km/h")
        elif velocidad<41:
            print("Aumente su velocida minimo permitido 41 km/h")
        else:
            print("Su velocidad es correcta")
    if zona == 3:
        if velocidad>120:
            print("Reduzca su velocidad maximo permitido 100 km/h")
        elif velocidad<61:
            print("Aumente su velocida minimo permitido 61 km/h")
        else:
            print("Su velocidad es correcta")


