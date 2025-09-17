from datetime import date

nombres =[]
edades = []

def ingresarNombre(nombre):
    nombres.append(nombre)

def ingresarEdad(anio):
    fechaActual = date.today()
    anioActual = fechaActual.year

    edad = anioActual-anio
    edades.append(edad)

def imprimirNombres ():
    
    print("Nombres de pacientes")

    for i in nombres:
        print(i)
        

def imprimirEdades ():
    
    print("Edades de pacientes")

    for i in edades:
       
        print(i)

def imprimirPacienteMayorMenor():
    edadMax = max(edades)
    edadMin = min(edades)
     
    edadMaxIndex = edades.index(edadMax)
    edadMinIndex = edades.index(edadMin)

    nombreMax = nombres[edadMaxIndex]
    nombreMin = nombres[edadMinIndex]
    print(f"{nombreMax} con la edad de {edadMax} es mayor a los demas pacientes")
    print(f"{nombreMin} con la edad de {edadMin} es menor a los demas pacientes")
