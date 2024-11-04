# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtrai(x, y):
    return x - y

# Função para multiplicação
def multiplica(x, y):
    return x * y

# Função para divisão
def divide(x, y):
    if y == 0:
        return "erro: divisão por zero!"
    return x / y

# Função principal
def calculadora():
    historico = []  # Lista para armazenar o histórico

    while(True): #menu de escolhas
        print("\nEscolha a ação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Divisão")
        print("4 - Multiplicação")
        print("5 - Histórico")
        print("6 - Sair")

        acao = input("Digite o número da operação desejada: ")

        if acao == '6':  # Sai do loop se o usuário digitar 6
            print("Saindo da calculadora.")
            break

        if acao == '5':  # Exibe o histórico se o usuário digitar 5
            print("\nHistórico das últimas 5 operações:")
            for operacao in historico:
                print(operacao)
            continue

        # Solicita os números para a operação
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação escolhida
        if acao == '1':
            resultado = soma(num1, num2)
            op_completa = f"{num1} + {num2} = {resultado}"

        elif acao == '2':
            resultado = subtrai(num1, num2)
            op_completa = f"{num1} - {num2} = {resultado}"

        elif acao == '3':
            resultado = divide(num1, num2)
            op_completa = f"{num1} / {num2} = {resultado}"

        elif acao == '4':
            resultado = multiplica(num1, num2)
            op_completa = f"{num1} * {num2} = {resultado}"

        else:
            print("Operação inválida")
            continue

        # Exibe o resultado da operação
        print("Resultado:", op_completa)

        # Adiciona a operação ao histórico, limitando a 5 operações
        historico.append(op_completa)
        if len(historico) > 5:
            historico.pop(0)  # Remove o item mais antigo se houver mais de 5 no histórico

# Executa a calculadora
calculadora()
