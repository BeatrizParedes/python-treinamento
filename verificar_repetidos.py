"Escreva um programa que leia 10 números inteiros e verifique se algum alor é repetido no array."
"Se houver repetições, exiba uma mensagem informando."

def repeticoes():
    numeros=[]
    for i in range (10):
        numero=int(input(f"Digite o numero {i+1}: ")) 
        numeros.append(numero)
    repetido=False
    for i in range(len(numeros)):         #O primeiro for fixa o elemento em i e o segundo percorre o próximo número para comparar
        for j in range(i+1,len(numeros)): #Não é uma matriz é uma comparação
            if numeros[i]==numeros[j]:
                repetido=True
                break
    if repetido:
        print("Há valores repetidos no array.")
    else:
        print("Não ha valores repetidos no array]")

if __name__=="__main__":
    repeticoes()