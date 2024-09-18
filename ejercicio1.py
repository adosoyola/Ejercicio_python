def calcular_mcd(a, b):
    """Función para calcular el máximo común divisor usando el algoritmo de Euclides."""
    while b:
        a, b = b, a % b
    return a

def obtener_numero_natural(mensaje):
    """Función para obtener un número natural del usuario con validación."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Por favor, ingrese un número natural (0 o positivo).")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número natural.")

def main():
    print("Cálculo del Máximo Común Divisor (MCD)")
    num1 = obtener_numero_natural("Ingrese el primer número natural: ")
    num2 = obtener_numero_natural("Ingrese el segundo número natural: ")
    
    mcd = calcular_mcd(num1, num2)
    print(f"El MCD de {num1} y {num2} es: {mcd}")

if __name__ == "__main__":
    main()
