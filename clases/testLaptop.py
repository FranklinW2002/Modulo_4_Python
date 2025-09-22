from laptop import Laptop
from laptopGaming import LaptopGaming
from laptopBussines import LaptopBusiness

def imprimirInforme(laptop):
    informe = laptop.realizarInformeUso()
    for clave,valor in informe.items():
        print(f"{clave} : {valor}")
    
    print("\n")

laptpPepitpo = Laptop("lenovo","i7",32)
laptpMaria= Laptop("lenovo","i7",32,600)

#for numero in range (1,1001):
#    asusLaptop = Laptop.asusLaptop(numero)
#   print(asusLaptop.__dict__)

#print(Laptop.compararCosto(laptpPepitpo,laptpMaria))
laptopGaming = LaptopGaming("Msi","i7",4,"RTX 8 GB")

#laptopNatalia = LaptopBusiness("MSI","i7",4,1000,2)
#print(laptopNatalia.realizarDiagnosticoSistema())
print("Laptop")
imprimirInforme(laptpPepitpo)
print("Laptop gamin")
imprimirInforme(laptopGaming)