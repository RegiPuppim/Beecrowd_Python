#Quanto vc ganha por hora?
valorHora = float(input())
#Quantas horas trabalhadas no mês
horaTrabalhada = float(input())
#Cálculo de Salário Bruto
salarioBruto = valorHora * horaTrabalhada
#Cálculo do Imposto de Renda
imposto = salarioBruto * 0.11
#Cálculo do INSS
inss =  salarioBruto * 0.08
#Cálculo do Sindicato
sindicato = salarioBruto * 0.05
#Cálculo do Salário Líquido
salarioLiquido = salarioBruto - imposto - inss - sindicato
print("Salário bruto: R$%.2f" "\nImposto: R$%.2f" "\nINSS: R$%.2f" "\nSindicato: R$%.2f" "\nLíquido: R$%.2f" % (salarioBruto, imposto, inss, sindicato, salarioLiquido))