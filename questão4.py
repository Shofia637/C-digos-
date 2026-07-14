soma = 0
quantidade = 0
maior = 0

numero = int(input("Digite um número: "))

while numero >= 0:
    soma = soma + numero
    quantidade = quantidade + 1

    if numero > maior:
        maior = numero

    numero = int(input("Digite outro número: "))

if quantidade > 0:
    media = soma / quantidade

    print("Soma:", soma)
    print("Média:", media)
    print("Maior número:", maior)
else:
    print("Nenhum número positivo foi informado.")