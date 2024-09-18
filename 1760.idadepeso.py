contadorPessoas = 1
contadorPeso = 0
somaIdade = 0
mediaIdade = 0

while contadorPessoas <= 4:
    idade = int(input())
    peso = float(input())
    if peso > 90:
        contadorPeso = contadorPeso + 1
    somaIdade = somaIdade + idade
    contadorPessoas = contadorPessoas + 1

mediaIdade = somaIdade / 4

print("Qtd pessoas > 90 Kg: %i" % contadorPeso)
print("Idade média: %.2f" % mediaIdade)
