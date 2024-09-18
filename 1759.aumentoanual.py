salarioInicial = 1000 #Salário inicial em 2005
taxaAumentoSalarial = 0.015 # Percentagem de aumento salarial em 2006

ano = int(input())
if ano < 2006:
    print("O ano informado deverá ser > 2005!")
else:
    x = 2006
    while x <= ano:
        novoSalario = salarioInicial + salarioInicial * taxaAumentoSalarial
        salarioInicial = novoSalario
        taxaAumentoSalarial = taxaAumentoSalarial + 0.01
        x = x + 1
    print("Salário atual: R$%.2f" % novoSalario)




