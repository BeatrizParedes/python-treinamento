"Desenvolva um programa que leia 5 números inteiros do usuário, armazene-os em um array e calcule a soma de todos os elementos."

def soma_array():
    numeros=[]
    soma=0

    for i in range(5):
        numero=int(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
        soma+=numero
    print(f"A soma dos elementos do array é: {soma}")

if __name__=="__main__":
    soma_array()