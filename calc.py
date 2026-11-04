def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    print("--- Calculadora CLI ---")
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    print(f"Soma: {somar(num1, num2)}")
    print(f"Subtração: {subtrair(num1, num2)}")
    print(f"Multiplicação: {multiplicar(num1, num2)}")