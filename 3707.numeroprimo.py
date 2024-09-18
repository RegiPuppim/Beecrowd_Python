numero = int(input())

if numero == 1:
    print("NÃO PRIMO")
else:
    i = 2
    divisor = 0

    while i * i <= numero:  # Verifica até a raiz quadrada do número
        if numero % i == 0:
            divisor = 1
        i += 1

    if divisor == 0:
        print("PRIMO")
    else:
        print("NÃO PRIMO")