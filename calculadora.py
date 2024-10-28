# Função para soma
def soma(x, y):
    return x + y


# Função para subtração
def subtrai(x, y):
    return x - y


# Função para divisão
def divide(x, y):
    if y == 0:
        return "erro: divisão por zero!"
    return x / y


# Função principal
def calculadora():
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")

    operacao = input("Digite o número da operação desejada: ")

    num1 = int(input("Digite o 1 número: "))
    num2 = int(input("Digite o 2 número: "))

    if operacao == '1':
        resultado = soma(num1, num2)
        op = "soma"
    elif operacao == '2':
        resultado = subtrai(num1, num2)
        op = "sub"
    elif operacao == '3':
        resultado = divide(num1, num2)
        op = "div"
    else:
        print("Operação inválida")

    print("Resultado da "+ op +": " + str(resultado))

# Executa a calculadora
calculadora()
