import math

casos_prueba = int(input())

for _ in range(casos_prueba):
    
    n1, _, d1, op, n2, _, d2 = input().split() #entrada de datos 
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)

    #condicionales para cada operador
    if op == "+":
        numerador = n1 * d2 + n2 * d1
        denominador = d1 * d2
    elif op == "-":
        numerador = n1*d2 - n2*d1
        denominador = d1 * d2
    elif op == "*":
        numerador = n1*n2 
        denominador = d1 * d2
    elif op == "/":
        numerador = n1 * d2
        denominador = n2 * d1

    mcd = math.gcd(numerador, denominador) #creacion del maximo comun divisor

    #variables simplificadas
    numerador_simplificado = numerador // mcd 
    denominador_simplificado = denominador // mcd
    print(f"{numerador} / {denominador} = {numerador_simplificado} / {denominador_simplificado}")