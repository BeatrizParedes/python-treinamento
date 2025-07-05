"Escreva um programa que leia um número inteiro e um número decimal do teclado e, em seguida, exiba a soma desses números no console"

def entrada_de_dados():
    num1 = int(input("Escreva um número inteiro: "))
    num2 = float(input("Escreva um numero decimal: "))

    print(f"A soma de {num1} + {num2} é: ",num1+num2)

if __name__=="__main__":
    entrada_de_dados()