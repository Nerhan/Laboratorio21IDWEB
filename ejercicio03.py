import math

class Figura:
    def area(self):
        raise NotImplementedError("Método area no implementado")
    
    def perimetro(self):
        raise NotImplementedError("Método perimetro no implementado")
    
    def __str__(self):
        return f"{self.__class__.__name__}: Área = {self.area():.2f}, Perímetro = {self.perimetro():.2f}"

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return self.largo * self.ancho
    
    def perimetro(self):
        return 2 * (self.largo + self.ancho)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio


figuras = [
    Rectangulo(5, 3),
    Triangulo(4, 3, 4, 5, 6),
    Circulo(2)
]

for figura in figuras:
    print(figura)