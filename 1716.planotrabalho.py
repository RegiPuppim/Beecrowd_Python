#Código do Plano de Trabalho: A, B ou C
codPlano = input()
#Salário Atual
salarioAtual = float(input())
#Salário final de acordo com o Plano de Trabalho
if codPlano == "A":
  salarioFinal = salarioAtual + salarioAtual * 0.1
  print("Novo salário: R$%.2f" % salarioFinal)
elif codPlano == "B":
  salarioFinal = salarioAtual + salarioAtual * 0.15
  print("Novo salário: R$%.2f" % salarioFinal)
elif codPlano == "C":
  salarioFinal = salarioAtual + salarioAtual * 0.2
  print("Novo salário: R$%.2f" % salarioFinal)
else:
  salarioFinal = salarioAtual