numeros = int(input())

contador = 1
somaPares = 0
while contador <= numeros:
    if contador % 2 ==0:
        somaPares = somaPares + contador
    contador = contador + 1

print(somaPares)