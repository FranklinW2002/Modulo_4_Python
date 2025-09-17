import informacion

cantidad = int(input("Ingrese la cantidad de pacientes a agregar"))

for i in range(cantidad):
    nombre = input("Ingrese nombre y apellido del paciente: ")
    informacion.ingresarNombre(nombre)
    anio = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    informacion.ingresarEdad(anio)

informacion.imprimirNombres()
informacion.imprimirEdades()
informacion.imprimirPacienteMayorMenor()