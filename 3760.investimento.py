investimentoInicial = float(input()) # em reais
taxaJurosAnual = float(input()) # em porcentagem
qtdAnos = int(input()) # numero de anos

totalTaxa = 0

for i in range(1,qtdAnos + 1):
    totalTaxa = (1+ (taxaJurosAnual/100)) ** i

valorFinal = investimentoInicial * totalTaxa

print("%.2f" % valorFinal)

