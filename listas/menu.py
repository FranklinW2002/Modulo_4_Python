menu = ["pollo","papas","sopa"]

plato =input("ingrese plato a añadir: ")

menu.append(plato)

plato =input("ingrese plato a buscar: ")

print(menu.index(plato))

plato =input("ingrese plato a eliminar: ")

menu.remove(plato)

print("MENU\n", menu)