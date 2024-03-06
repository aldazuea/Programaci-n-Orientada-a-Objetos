
class Usuario:
    def __init__(self, nombre, apellido, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro

    def prestar_libro(self, titulo, usuario):
        libro = self.buscar_libro(titulo)
        if libro and not libro.prestado:
            libro.prestado = True
            return True
        return False

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro and libro.prestado:
            libro.prestado = False
            return True
        return False

# Crear usuarios
usuario1 = Usuario("Juan", "Perez", 30, "juan@example.com")
usuario2 = Usuario("Maria", "Gomez", 25, "maria@example.com")

# Crear libros
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "9789876123133")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "9788439722330")

# Crear biblioteca
biblioteca = Biblioteca()

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Agregar libros al catálogo
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Prestar y devolver libros
biblioteca.prestar_libro("El principito", usuario1)
biblioteca.devolver_libro("El principito")

# Buscar en el catálogo
print(biblioteca.buscar_libro("Cien años de soledad"))