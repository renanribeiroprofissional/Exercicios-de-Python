# 2. Calculadora de 4 Operações

# Escreve um programa em javascript que permita inserir dois valores numéricos e então calcule o resultado das quatro operações básicas (soma, subtração, multiplicação e divisão).

# Após calcular os resultados o programa deve exibi-los na tela.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = (n1 + n2)
subtracao = (n1 - n2)
multiplicacao = (n1 * n2)
divisao = (n1 / n2)

print("\n"+"Soma: "+str(soma) +"\n"+"Subtração: "+ str(subtracao) +"\n"+"Multiplicação: "+ str(multiplicacao) +"\n"+"Divisão: "+ str(divisao))
