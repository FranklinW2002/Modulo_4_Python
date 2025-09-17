from Auto import Auto

autoFranklin = Auto.autoAudi()
autoMateo = Auto.autoToyota()

print(autoFranklin.__dict__)
print(autoMateo.__dict__)
print(Auto.compararKilometrage(autoFranklin,autoMateo))
print(Auto.compararMarca(autoFranklin,autoMateo))