# Função para somar
def somar(a, b):
    return a + b

# Função para subtrair
def subtrair(a, b):
    return a - b

# Função para multiplicar
def multiplicar(a, b):
    return a * b

# Função para dividir
def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

# Testando as funções
num1 = 10
num2 = 5

print(f"Soma: {num1} + {num2} = {somar(num1, num2)}")
print(f"Subtração: {num1} - {num2} = {subtrair(num1, num2)}")
print(f"Multiplicação: {num1} * {num2} = {multiplicar(num1, num2)}")
print(f"Divisão: {num1} / {num2} = {dividir(num1, num2)}")