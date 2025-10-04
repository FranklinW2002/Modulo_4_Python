from abc import ABC, abstractmethod

class empleado(ABC):
    def __init__(self, nombre, salariobase):
        self.nombre = nombre
        self.salariobase = salariobase

    @abstractmethod
    def calcularsalario(self):
        pass


class EmpleadoTiempoCompleto(empleado):
    def calcularsalario(self):
        return self.salariobase * 1.20  


class EmpleadoMedioTiempo(empleado):
    def calcularsalario(self):
        return self.salariobase*1.10
    
empleado1 = EmpleadoTiempoCompleto("Carlos", 1000)
empleado2 = EmpleadoMedioTiempo("Ana", 800)

print(f"{empleado1.nombre} - Salario final: {empleado1.calcularsalario()}")
print(f"{empleado2.nombre} - Salario final: {empleado2.calcularsalario()}")

empleados = [empleado1, empleado2, EmpleadoTiempoCompleto("Lucía", 1200), EmpleadoMedioTiempo("Pedro", 700)]

print("\nSalarios de todos los empleados:")
for e in empleados:
    print(f"{e.nombre} - Salario final: {e.calcularsalario()}")