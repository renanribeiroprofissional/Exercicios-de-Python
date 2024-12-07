# Teste de Velocidade

# Escreva um programa em javascript que permita inserir o nome e a velocidade de dois veículos e exiba na tela uma mensagem dizendo qual dos dois é mais rápido (ou que as velocidades são iguais se este for o caso)

car1 = input("Digite um nome para seu carrinho: ")
velocidade1 = int(input("Digite a velocidade do "+ car1))

car2 = input("Digite o nome do seu carrinho: ")
velocidade2 = int(input("Digite a velocidado do "+ car2))


if velocidade1 > velocidade2:
  print(car1 +" é mais rapido que "+ car2)
elif velocidade2 > velocidade1:
    print(car2 + " é mais rapido que "+ car1)
elif velocidade1 == velocidade2:
    print(car1 +" e " +car2 + " tem a mesma velocidade")
else: print("Obrigado")

