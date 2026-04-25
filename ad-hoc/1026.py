
casos_prueba = int(input())

#funcion principal
def ruleta():
    for _ in range(casos_prueba):
        personas = int(input())
        saltos = int(input())
        personas = list(range(1, personas + 1))

        while len(personas) > 1:
            del personas [1]
    print(personas)

ruleta()