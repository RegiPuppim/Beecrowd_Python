nivel = int(input())
horasAulas = float(input())
if nivel == 1:
    salario = 12.00 * horasAulas
    print("Seu salário é de R$%.2f" % salario)
elif nivel == 2:
    salario = 17.00 * horasAulas
    print("Seu salário é de R$%.2f" % salario)
elif nivel == 3:
    salario = 25.00 * horasAulas
    print("Seu salário é de R$%.2f" % salario)
else:
    print("O nível digitado não é válido!")

