n = int(input())

def fibonacci(n):
    secuencia =[]
    if n == 0:
        secuencia = [0]
    elif n == 1:
        secuencia = [0, 1]
    elif n > 1:
        secuencia = [0, 1 ]
        a, b = 0, 1
        for _ in range(n-2): 
            
            a, b = b, a + b
            secuencia.append(b)
        
    print(*secuencia)

    
        


if n <= 46:
    fibonacci(n)
