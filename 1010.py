entrada_1 = input().split(" ")
entrada_2 = input().split(" ")

cod1, qtde1, valor1 = entrada_1
cod2, qtde2, valor2 = entrada_2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)