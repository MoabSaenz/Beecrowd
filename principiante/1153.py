n = int(input())

def factorial(n):
    if n <= 13:
        resultado = 1

        for i in range(1, n + 1):
            resultado *= i

        print(resultado)

factorial(n)