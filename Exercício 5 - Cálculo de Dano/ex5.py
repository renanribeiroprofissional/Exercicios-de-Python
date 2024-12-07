# Cálculo de Dano

# Escreva um programa que permita inserir o nome e o poder de ataque de um personagem, depois o nome, a quantidade de pontos de vida, o poder de defesa de outro personagem e se ele possui um escudo, e então calcule a quantidade de dano causado baseado nas seguintes regras:

# Se o poder de ataque for maior do que a defesa e o defensor não possuir um escudo, o dano causado será igual a diferença entre o ataque e a defesa.

# Se o poder de ataque for maior do que a defesa e o defensor possuir um escudo, o dano causado será igual a metade da diferença entre o ataque e a defesa.

# Se o poder de ataque for menor ou igual a defesa, o dano causado será 0.

# Por fim, o programa deve subtrair a quantidade de dano da quantidade de pontos de vida do personagem defensor e exibir na tela a quantidade de dano e as informações atualizadas de ambos os personagens.


danoCausado = 0

# Ataque:
nomeAtaque = input("Digite o nome do personagem de ataque: ")
ataque = int(input("Digite a quantidade de poder de ataque: "))

# Defesa:

nomeDefesa = input("Digite o nome do personagem de defesa: ")
vida = int(input("Digite a quantidade de pontos de vida do personagem: "))
defesa = int(input("Digite a quantidade de pontos de defesa do personagem: "))
escudo = input("O personagem possui escudo? Sim/Não: ")

if ataque > defesa and escudo == "Não":
    danoCausado = ataque - defesa

elif ataque > defesa and escudo == "Sim":
    danoCausado = (ataque - defesa) / 2

elif ataque <= defesa:
    danoCausado = 0

vida -= danoCausado

print("\n"+nomeAtaque+" Causou "+ str(danoCausado)+ " em "+nomeDefesa)
print("\n"+nomeAtaque + "\nAtaque: "+ str(ataque))
print("\n"+nomeDefesa+"\nVida: "+str(vida)+"\nDefesa: "+str(defesa)+"\nEscudo: "+str(escudo))
