class libro:

    contador_libros = 0

    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas

        libro.contador_libros += 1
    def mostrar_info(self):
        return self.titulo,self.autor,self.paginas

    @staticmethod
    def es_grade(libro):
        if libro.paginas>300:
            return True
        else:
            return False
        
    @classmethod
    def total_libros(cls): 
        return cls.contador_libros
    



    pass

libro1 = libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro2 = libro("El Principito", "Antoine de Saint-Exupéry", 96)
libro3 = libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

print(f"Libro1: {libro1.mostrar_info()}")
print(f"Libro1: {libro2.mostrar_info()}")
print(f"Libro1: {libro3.mostrar_info()}")

print(f"¿'{libro1.titulo}' es grande?:", libro.es_grade(libro1))
print(f"¿'{libro2.titulo}' es grande?:", libro.es_grade(libro2))
print(f"¿'{libro3.titulo}' es grande?:", libro.es_grade(libro3))


print("Total de libros creados:", libro.total_libros())