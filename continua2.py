# JOGO DE ADIVINHACAO DE PALAVRAS

palavra = "PYTHON"

letras_descobertas = []
letras_utilizadas = []

erros = 0
limite_erros = 6

print("=" * 35)
print("       JOGO DE ADIVINHACAO")
print("=" * 35)

while erros < limite_erros:

    # Exibe a palavra parcialmente descoberta
    print("\nPalavra: ", end="")

    for letra in palavra:
        if letra in letras_descobertas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"\nErros: {erros}/{limite_erros}")

    # Verificar se o jogador descobriu a palavra
    if len(letras_descobertas) == len(palavra):
        break

    # Pedir o palpite e guardar numa string
    palpite = input("Digite uma letra: ")
    palpite = palpite.upper()

    # Validar a entrada
    if len(palpite) != 1:
        print("Digite apenas uma letra!")
    elif not palpite.isalpha():
        print("Digite apenas letras!")
    elif palpite in letras_utilizadas:
        print("Você já utilizou essa letra!")

    else:

        # Adicionar a letra na lista de utilizadas
        letras_utilizadas.append(palpite)

        # Verificar se a letra existe na palavra
        if palpite in palavra:
            letras_descobertas.append(palpite)
            print("Você acertou!")
        else:
            print("Você errou!")
            erros = erros + 1

# Resultado final
print("\n" + "=" * 35)

# Verificar se a pessoa ganhou ou perdeu
if len(letras_descobertas) == len(palavra):
    print("Parabéns! Você descobriu a palavra!")
else:
    print("Você perdeu! Acabaram as tentativas.")

print(f"A palavra secreta era: {palavra}")

print("=" * 35)