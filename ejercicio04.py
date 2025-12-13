class Libro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponible = True
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"'{self.titulo}' ha sido prestado."
        else:
            return f"'{self.titulo}' no está disponible."
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"'{self.titulo}' ha sido devuelto."
        else:
            return f"'{self.titulo}' ya está disponible."
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} ({self.ano}) - {estado}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, ano, formato, tamano_mb):
        super().__init__(titulo, autor, ano)
        self.formato = formato
        self.tamano_mb = tamano_mb
    
    def prestar(self):
        return f"'{self.titulo}' (digital) ha sido prestado (siempre disponible)."
    
    def __str__(self):
        return super().__str__() + f" - Formato: {self.formato}, Tamaño: {self.tamano_mb} MB"

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def listar_libros(self):
        for libro in self.libros:
            print(libro)
    
    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")
    
    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(libro.prestar())
                return
        print(f"No se encontró el libro '{titulo}'.")

biblioteca = Biblioteca()

libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)

libro_digital1 = LibroDigital("Python for Beginners", "John Doe", 2020, "PDF", 5.2)
libro_digital2 = LibroDigital("Advanced Web Dev", "Jane Smith", 2022, "EPUB", 3.8)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro_digital1)
biblioteca.agregar_libro(libro_digital2)

print("Listar todos los libros:")
biblioteca.listar_libros()
print("\n")

print("Prestar un libro físico:")
biblioteca.prestar_libro("1984")
print("\n")

print("Prestar un libro digital 5 veces:")
for _ in range(5):
    biblioteca.prestar_libro("Python for Beginners")
print("\n")

print("Intentar prestar un libro ya prestado:")
biblioteca.prestar_libro("1984")
print("\n")

print("Buscar libros por autor (George Orwell):")
biblioteca.buscar_por_autor("George Orwell")
print("\n")