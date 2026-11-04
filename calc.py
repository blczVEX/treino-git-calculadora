def somar(a, b):
    return a + b

if __name__ == "__main__":
    print("--- Calculadora CLI ---")
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    print(f"Soma: {somar(num1, num2)}")
    