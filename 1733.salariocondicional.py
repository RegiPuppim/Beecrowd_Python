nome = input()
horasExtras = float(input())
salarioMinimo = 1192.40
valorHoraExtra = 10.00
salarioHoraExtra = horasExtras * valorHoraExtra
salarioBruto = 3 * salarioMinimo + salarioHoraExtra
if salarioBruto > 2000.00:
    inss = salarioBruto * 0.12
else:
    inss = salarioBruto * 0.05
if salarioBruto > 2500.00:
    impostoRenda = salarioBruto * 0.2
else:
    impostoRenda = 0.00
salarioLiquido = salarioBruto - inss - impostoRenda
print("Nome: %s" % (nome))
print("Salário bruto: R$%.2f" % (salarioBruto))
print("Salário líquido: R$%.2f" % (salarioLiquido))