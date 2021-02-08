print("*********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = int(43)

chute_str = input("digite o seu número: ")

print("você digitou ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("você acertou")
else:
    if(maior):
        print("você errou! o seu chute foi maior do que o número secreto")
    elif(menor):
        print("você errou! o seu chute foi menor do que o número secreto")

print("fim do jogo")