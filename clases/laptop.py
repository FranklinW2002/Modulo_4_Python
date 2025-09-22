import random

class Laptop:
    def __init__(self,marca,procesador,memoria,costo=500,inmpuesto=10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.inmpuesto = inmpuesto

    def valorFinal(self):
        return self.costo + self.inmpuesto
    
    def valorDescuento(self,descuento):
        return (self.costo * descuento)/100
    
    def realizarDiagnosticoSistema(self):
        resultado = {
            "Marca" : f"{self.marca}",
            "Procesador": f"{self.procesador}",
            "Memoria ram": "OK" if self.memoria >= 8 else "Aumentar memoria ram",
            "Bateria": "Ok" if random.choice([True,False])else "Cambiar de bateria"

        }
        return resultado
    
    def compararCosto(laptop1,laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales"
        else:
            return "Los costos son diferentes"
    
    def realizarInformeUso(self):
        resultadoInforme={
            "Tipo de uso" : "Generica",
            "Uso recomendado" : "Tareas cotidianas",
            "Horas de uso" : 5,
            "Diagnostico actual" : self.realizarDiagnosticoSistema()
        }
        return resultadoInforme

    @classmethod
    def asusLaptop(cls,costo):
        marca = "asus"
        procesador = "i5"
        memoria = "16"
        return cls(marca,procesador,memoria,costo)