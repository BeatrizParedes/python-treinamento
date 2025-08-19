"Escreva um programa que leia 10 números inteiros e verifique se algum valor é repetido no array."
"Se houver repetições, exiba uma mensagem informando."

def repeticoes():
    numeros=[]
    for i in range (10):
        numero=int(input(f"Digite o número {i+1} "))
        numeros.append(numero)

    verificar=int(input(f"Qual número deseja verificar? "))
    encontrado=False
    for i in range(len(numeros)):
        if numeros[i]==verificar:
            encontrado=True
    if encontrado:
        print (f"O número {verificar} foi encontrado")
    else:
        print (f"O número não foi encontrado")

if __name__=="__main__":
    repeticoes()