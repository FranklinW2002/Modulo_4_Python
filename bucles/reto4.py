datos = []

cantidad = int(input("Ingrese la cantidad de datos a agregar ----> "))

for i in range(cantidad):
    valor = input(f"Ingrese su elemento {i+1}: " )
    try:
        numero = float(valor)
        datos.append(numero)
    except ValueError:
        datos.append(valor)

print(f"Su lista es {datos}")        
