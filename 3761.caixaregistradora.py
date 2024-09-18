tipoItens = int(input()) # qtd de ítens diferentes a serem registrados

valorTotal = 0
for item in range (0,tipoItens):
    valorUnitario = float(input()) # preço unitário do ítem
    qtdItens = int(input()) # qtd comprada do ítem
    valorTotal += qtdItens * valorUnitario # valor total da compra

desconto = float(input()) # desconto em % concedido ao final da compra

valorDesconto = valorTotal * (desconto/100) # valor em R$ do desconto

valorFinal = valorTotal - valorDesconto # valor total da compra com desconto

print("Total: R$ %.2f" % valorTotal)
print("Desconto: R$ %.2f" % valorDesconto)
print("Valor final: R$ %.2f" % valorFinal)
