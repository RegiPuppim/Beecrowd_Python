#Preço de compra do produto
valorCompra = float(input())
#Condição
if valorCompra < 20:
    valorVenda = valorCompra + valorCompra * 0.45
else:
    valorVenda = valorCompra + valorCompra * 0.3
#Valor de venda na tela
print("Valor de venda: R$%.2f" % valorVenda)

