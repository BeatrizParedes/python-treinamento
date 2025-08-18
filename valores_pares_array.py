"Crie um programa que leia 8 números inteiros e exiba todos os valores pares armazenados no array"

def pares_array():
    numeros=[]

    for i in range (8):
        numero=int(input(f"Digite o numero {i+1}: "))
        numeros.append(numero)

    for numero in numeros:
        if numero%2==0:
            print(numero)

if __name__=="__main__":
    pares_array()