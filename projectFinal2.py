while True:
    num1 = float(input("Digite o primeiro valor\n"))
    num2 = float(input("Digite o segundo valor\n"))
    operador = str(input("Digite o tipo de Operação: + - * /\n"))

    def somar(num1,num2):
        return "Seu resultado foi:\n" + str(num1+num2) + "\nReiniciando...\n"
    def subtrair(num1,num2):
        return "Seu resultado foi:\n" + str(num1-num2) + "\nReiniciando...\n"
    def multiplicar(num1,num2):
        return "Seu resultado foi:\n" + str(num1*num2) + "\nReiniciando...\n"
    def dividir(num1,num2):
        return "Seu resultado foi:\n" + str(num1/num2) + "\nReiniciando...\n"

    if operador == "+":
        print(somar(num1,num2))
    elif operador == "-":
        print(subtrair(num1,num2))
    elif operador == "*":
        print(multiplicar(num1,num2))
    elif operador == "/":
        print(dividir(num1,num2))
    else:
        print("Operação inválida, finalizando...")
        exit()