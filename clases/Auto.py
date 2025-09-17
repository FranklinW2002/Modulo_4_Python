
class Auto:
    def __init__(self,marca,modelo,año,kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
       
    def mostrarInformacion(self):
            print(f"\nMarca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Año: {self.año}")
            print(f"Kilometraje: {self.kilometraje}")

    def actualizarKilometraje(self,kilometrajeNuevo):
        if self.kilometraje < kilometrajeNuevo:
            self.kilometraje = kilometrajeNuevo
        else:
            print("No se puede disminuir el kilometraje")
        
    def realizarViaje(self,kilometros):
        if kilometros >= 0:
            self.kilometraje = self.kilometraje + kilometros
        else:
            print("La cantidad de kilometros deben ser positivos")
        
    def estadoAuto(self):
        if self.kilometraje < 2000:
            print("Estoy como nuevo")
        elif self.kilometraje>=2000 and self.kilometraje < 100000:
            print("Ya estoy usado")
        elif self.kilometraje > 100000:
            print("¡Ya dejame descansar porfavor!") 
    @staticmethod
    def compararKilometrage(auto1,auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        else:
            return "No tienen el mismo kilometrage"

    @staticmethod
    def compararMarca(auto1,auto2):
        if auto1.marca == auto2.marca:
            return "Son de la misma marca"
        else:
            return "No son de la misma marca"

    @classmethod
    def autoToyota(cls):
        marca = "Toyota"
        modelo = "Hilux"
        año = "2025"
        return cls(marca,modelo,año)

    @classmethod
    def autoAudi(cls):
        marca = "audi"
        modelo = "r8"
        año = "2020" 
        return cls(marca,modelo,año)

