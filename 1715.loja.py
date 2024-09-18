#Código da pessoa: 1(cliente comum),2(funcionários) ou 3(cliente premium)
codPessoa = int(input())
#Valor da compra
valorCompra = float(input())
#Valor total de acordo com o código da pessoa
if codPessoa == 1:
  valorTotal = valorCompra
  print("Valor total a ser pago: R$%.2f" % valorTotal)
elif codPessoa == 2:
  valorTotal = valorCompra - valorCompra * 0.13
  print("Valor total a ser pago: R$%.2f" % valorTotal)
elif codPessoa == 3:
  valorTotal = valorCompra - valorCompra * 0.07
  print("Valor total a ser pago: R$%.2f" % valorTotal)
else:
  print("OPÇÃO INVÁLIDA!")



