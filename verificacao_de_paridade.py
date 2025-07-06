"Escreva um programa que leia um número inteiro e exiba se ele é par ou ímpar"
"Dica: Você pode utilizar a divisao de resto, com o operador %"

def paridade():
    
    num = int(input("Escreva um número inteiro: "))
    if (num%2==0):
        print(f"O {num} é um número par")
    else:
        print(f" O {num} é um número ímpar")

if __name__=="__main__":
    paridade()


