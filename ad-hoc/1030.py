casos_prueba = int(input())

def ruleta():
    for caso in range(1, casos_prueba + 1):
        n, k = map(int, input().split())
        
        personas = list(range(1, n + 1))
        index = 0
        
        while len(personas) > 1:
            index = (index + k - 1) % len(personas)
            personas.pop(index)
        
        print(f"Case {caso}: {personas[0]}")

ruleta()