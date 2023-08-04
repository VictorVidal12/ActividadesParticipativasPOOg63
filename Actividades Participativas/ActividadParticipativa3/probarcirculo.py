from clases import Punto, Circulo

centro = Punto(4, 4)
circulo = Circulo(centro, 4)
print(circulo.calcular_area_circulo())
print(circulo.calcular_perimetro_circulo())
punto = Punto(16, 4)
circulo.pertenece_al_circulo(punto)
