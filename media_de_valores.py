"Escreva um programa que leia 10 números inteiros e calcule a média dos valores inseridos utilizando um array para armazenar os números"

def media_array():
    numeros=[]
    soma=0
    media=0

    for i in range (10):
        numero=int(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
        soma+=numero
    media=soma/len(numeros)
    print(f"A média dos valores é: {media}")

if __name__=="__main__":
    media_array()