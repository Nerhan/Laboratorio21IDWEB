import ejercicio03

def main():
    print("===IMPORTANDO===")
    
    rect = ejercicio03.Rectangulo(10, 5)
    tri = ejercicio03.Triangulo(8, 6, 8, 8, 8)
    circ = ejercicio03.Circulo(4)
    
    figuras = [rect, tri, circ]
    
    for figura in figuras:
        print(figura)
    
    print(f"\nDetalles del rectángulo: largo={rect.largo}, ancho={rect.ancho}")
    print(f"Detalles del círculo: radio={circ.radio}")

if __name__ == "__main__":
    main()