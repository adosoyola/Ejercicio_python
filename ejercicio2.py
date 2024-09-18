#Ejercicio 2
def calcular_mcd(a, b):
    """Función para calcular el máximo común divisor usando el algoritmo de Euclides."""
    while b:
        a, b = b, a % b
    return a

def obtener_numero_entero(mensaje):
    """Función para obtener un número entero del usuario con validación."""
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def main():
    print("Cálculo del Máximo Común Divisor (MCD)")
    num1 = obtener_numero_entero("Ingrese el primer número entero: ")
    num2 = obtener_numero_entero("Ingrese el segundo número entero: ")
    
    mcd = calcular_mcd(abs(num1), abs(num2))  # Usamos el valor absoluto para el MCD
    print(f"El MCD de {num1} y {num2} es: {mcd}")

if __name__ == "__main__":
    main()
