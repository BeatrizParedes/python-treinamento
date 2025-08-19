"Escreva um programa que crie um array de 5 números inteiros e multiplique todos os seus valores por 2, exibindo o novo array no console"

def duplicacao():
    numeros=[]
    for i in range (5):
        resto=5-i
        numero=int(input(f"Digite o numero {i+1}, (restam {resto}) "))
        numeros.append(numero)
    for i in range(len(numeros)):
        numeros[i]*=2
        print(numeros[i])

if __name__=="__main__":
    duplicacao()