"Desenvolva um programa que leia três números inteiros e exiba o maior deles"

def maior():
    num1=int(input("Escolha o primeiro número: "))
    num2=int(input("Escolha o segundo número: "))
    num3=int(input("Escolha o terceiro número: "))

    if (num1>num2&num1>num3):
        print(f"O {num1} é o maior número entre os que você escolheu")
    elif (num2>num1&num2>num3):
        print(f"O {num2} é o maior número entre os que você escolheu")
    else:
        print(f"O {num3} é o maior dos números que você escolheu") #Se o f não for colocado o programa mantém a variável nas chaves e não atribui o valor

if __name__=="__main__":
    maior()