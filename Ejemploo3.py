def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def main():
    largo_rect = 4
    ancho_rect = 6
    area_rectangulo = calcular_area_rectangulo(largo_rect, ancho_rect)
    print(f"Área del rectángulo: {area_rectangulo}")

    base_triang = 5
    altura_triang = 8
    area_triangulo = calcular_area_triangulo(base_triang, altura_triang)
    print(f"Área del triángulo: {area_triangulo}")

main()
