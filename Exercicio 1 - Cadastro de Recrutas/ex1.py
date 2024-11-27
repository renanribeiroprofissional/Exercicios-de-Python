# ## 1. Cadastro de Recrutas

# Escreva um programa em javascript que permita salvar informações de um recruta. As informações a serem salvas são:

# o primeiro nome
nome = input("Digite seu nome: ")

# o sobrenome
sobrenome = input("Digite o seu sobrenome: ")

# o campo de estudo
estudo = input("Qual seu curso ? ")

# o ano de nascimento
nascimento = int(input("Digite seu ano de nascimento "))

idade = 2024 - nascimento

# Depois o programa deve exibir o nome completo do recruta, seu campo de estudo e sua idade (apenas baseada no ano de nascimento).

print("Seu nome é "+ nome +" "+sobrenome+ ", você estuda "+ estudo+" e você têm "+str(idade)+" anos.")
