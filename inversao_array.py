"Crie um programa que leia 6 números inteiros e armazene-os em um array."
"Depois, exiba os valores do array na ordem inversa"

def inversao_array():
    numeros=[]

    for i in range(6):
        resto=6-i
        numero=int(input(f"Digite o número {i+1} (restam: {resto})" ))
        numeros.append(numero)

    print ("Números em ordem inversa:")
    for i in range (len(numeros)-1,-1):
        print(numeros[i])

if __name__=="__main__":
    inversao_array()