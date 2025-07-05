"Desenvolva um programa que declare duas variáveis inteiras e realize as operações de:"
"Soma, subtração, multiplicação, divisão e módulo entre elas"
"Exiba os resultados de cada operação"

def calculadora():
    num1 = float (input("Insira o primeiro número "))
    num2 = float (input("Insira o segundo número "))
    
    print(f"{num1} - {num2} = ", num1-num2)
    print(f"{num1} + {num2} = ", num1+num2)
    print(f"{num1} * {num2} = ", num1*num2)
    print(f"{num1} / {num2} = ", num1/num2)
    print(f"{num1} % {num2} = ", num1%num2) #Operação de módulo retorna o resto da divisão de num1 por num2

if __name__ == "__main__":
    calculadora()