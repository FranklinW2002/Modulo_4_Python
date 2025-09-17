from laptop import Laptop

laptpPepitpo = Laptop("lenovo","i7",32)
laptpMaria= Laptop("lenovo","i7",32,600)

for numero in range (1,1001):
    asusLaptop = Laptop.asusLaptop(numero)
    print(asusLaptop.__dict__)

#print(Laptop.compararCosto(laptpPepitpo,laptpMaria))