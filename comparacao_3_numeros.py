"Desenvolva um programa que leia três números inteiros e exiba o maior deles."
"Caso dois ou mais números sejam iguais, exiba uma mensagem indicando que há números iguais"

def comparacao():
    num1 = int(input("Escreva o primeiro número: "))
    num2 = int(input("Escreva o segundo número: "))
    num3 = int(input("Escreva o terceiro número: "))

    if (num1>num2 and num1>num3):
        print(f"O {num1} é o maior número fornecido")
    elif (num2>num1 and num2>num3):
        print(f"O {num2} é o maior número fornecido")
    else:
        print(f"O {num3} é o maior número fornecido ")
    
    if (num1==num2 or num1==num3):
        print("Há números iguais")

if __name__=="__main__":
    comparacao()