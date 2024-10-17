# Roteiro de prática

# Variável para controlar a saída do programa
saida = ''

# Função de adição
def adicao(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora que receber os valores e qual operação realizar
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço para continuar a execução enquanto o usuário desejar ou encerrar o programa
while saida.lower() != 'n':
    # Solicitando os números e a operação do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, / ou adicao, subtracao, multiplicacao, divisao): ")
    
    # Chamada da função calculadora
    resultado = calculadora(num1, num2, operacao)
    
    # Exibindo o resultado
    print(f"Resultado da operação: {resultado}")
    
    # Pergunta ao usuário se ele deseja continuar
    saida = input("Deseja continuar? (S/N): ")
