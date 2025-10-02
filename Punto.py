import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "1er cuadrante"
        elif self.x < 0 and self.y > 0:
            return "2º cuadrante"
        elif self.x < 0 and self.y < 0:
            return "3er cuadrante"
        elif self.x > 0 and self.y < 0:
            return "4º cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)


# Ejemplo de uso

A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)

print("Cuadrante de A:", A.cuadrante())
print("Cuadrante de B:", B.cuadrante())
print("Cuadrante de C:", C.cuadrante())
print("Cuadrante de D:", D.cuadrante())

print("Vector de A a B:", A.vector(B))
print("Vector de B a A:", B.vector(A))

print("Distancia entre A y B:", round(math.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2), 3))
print("Distancia entre A y C:", round(math.sqrt((C.x - A.x) ** 2 + (C.y - A.y) ** 2), 3))
print("Distancia entre B y C:", round(math.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2), 3))

class Rectangulo:
    def __init__(self, punto_inicial=None, punto_final=None):
        # Si no se envían puntos, se crean en el origen
        self.punto_inicial = punto_inicial if punto_inicial else Punto()
        self.punto_final = punto_final if punto_final else Punto()

    def base(self):
        # Base = diferencia absoluta en X
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        # Altura = diferencia absoluta en Y
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()


# Ejemplo de uso para Rectangulo
rect = Rectangulo(A, B)

print("Base del rectángulo:", rect.base())
print("Altura del rectángulo:", rect.altura())
print("Área del rectángulo:", rect.area())
