def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    print("Calculadora básica")
    print("Operaciones disponibles: suma, resta, multiplicación, división")
    op = input("Elige una operación (+, -, *, /): ")
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if op == "+":
        print("Resultado:", sumar(a, b))
    elif op == "-":
        print("Resultado:", restar(a, b))
    elif op == "*":
        print("Resultado:", multiplicar(a, b))
    elif op == "/":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()