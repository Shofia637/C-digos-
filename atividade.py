
import random

while True:

    print("JOGO DE ADIVINHAÇÃO")
    print("1 - De 1 a 10")
    print("2 - De 1 a 20")
    print("3 - De 1 a 30")

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        maior = 10
    elif nivel == 2:
        maior = 20
    else:
        maior = 30

    numero = random.randint(1, maior)

    tentativa = 1
    acertou = False

    while tentativa <= 3:

        chute = int(input("Digite um número: "))

        if chute == numero:
            print("Parabéns, você acertou!")
            acertou = True
            break

        print("Você errou!")

        if chute < numero:
            print("Tente um número maior")
        else:
            print("Tente um número menor")

        tentativa = tentativa + 1

    if acertou == False:
        print("Você perdeu! Fim de jogo.")
        print("O número sorteado foi:", numero)

    jogar = input("Quer jogar novamente? : ")

    if jogar !=
        break