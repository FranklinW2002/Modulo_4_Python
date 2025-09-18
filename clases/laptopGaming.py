from laptop import Laptop

class LaptopGaming(Laptop):
    def __init__(self, marca, procesador, memoria,targetaGrafica, costo=500, inmpuesto=10):
        super().__init__(marca, procesador, memoria, costo, inmpuesto)
        self.targetaGrafica = targetaGrafica

    def realizarDiagnosticoSistema(self):
        resultadoDiagnostico = super().realizarDiagnosticoSistema()
        resultadosJuegos = self.realizarDiagnosticoJuegos()
        resultadoDiagnostico["Resultados juegos"] = resultadosJuegos
        return resultadoDiagnostico
    
    def realizarDiagnosticoJuegos(self):
        juegos = ["Fornite","COD","GTA"]
        resultados = {}
        for juego in juegos:
            fpsBase = 30
            if "RTX" in self.targetaGrafica:
                fps = fpsBase*3
            elif "GTX" in self.targetaGrafica:
                fps = fpsBase*2
            else:
                fps = fpsBase
            resultados[juego] = f"{fps} FPS"
        return resultados
    pass