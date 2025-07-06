"Escreva um programa que leia um número inteiro e verifique se ele está entre 10 e 20 (inclusive)"
"Exiba uma mensagem informando se o número está dentro ou fora do intervalo"

def intervalo():
    num1 = int(input("Escolha o número para verificar se está dentro do intervalo 10 e 20: "))
    
    if (10<=num1<=20):
        print(f"{num1} está dentro do intervalo")
    else:
        print(f"{num1} está fora do intervalo")

if __name__ =="__main__":
    intervalo()