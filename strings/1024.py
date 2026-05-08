#ENCRIPTACION 
casos_prueba = int(input())
for _ in range(casos_prueba):
    palabra = input()
    palabra = list(palabra)

    palabra_encriptada = []

    for letra in palabra:
        if letra.isalpha():
            nueva_letra = chr(ord(letra) + 3)
            palabra_encriptada.append(nueva_letra)
            
        else:
            nueva_letra = letra
            palabra_encriptada.append(nueva_letra)
    
    palabra_encriptada.reverse()

    inicio = len(palabra_encriptada) // 2 

    for i in range(inicio, len(palabra_encriptada)):

        nueva_letra = chr(ord(palabra_encriptada[i]) - 1)    
        palabra_encriptada[i] = nueva_letra

    
    print("".join(palabra_encriptada))
        
