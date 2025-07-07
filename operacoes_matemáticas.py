"Desenvolva um programa que leia dois números e um operador (+,-,*,/)"
"Realize a operação correspondente"
"Exiba o resultado no console"

def operacoes():
    num1=float(input("Escreva o primeiro número: "))
    operador=input("Escreva qual operador gostaria de usar: ")
    num2=float(input("Escreva o segundo número: "))

    if (operador=='+'):
        print(f"{num1} + {num2}=", num1+num2)
    elif (operador=='-'):
        print(f"{num1} - {num2}=", num1-num2)
    elif (operador=='*'):
        print(f"{num1} * {num2}=", num1*num2)
    elif (operador=='/'):
        if (num2 !=0):
            print(f"{num1} / {num2} = ", num1/num2)
        else:
            print("Divisão por zero não é permitida")
    else:
        print("Operador inválido")

if __name__=="__main__":
    operacoes()