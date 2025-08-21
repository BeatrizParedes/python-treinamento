"Desenvolva um programa que crie dois arrays de 5 números inteiros."
"O programa deve comparar os dois arrays e exibir quais posições possuem valores iguais."

def comparacao():
    numeros=[]
    numeros2=[]
    for i in range(5):
        numero=int(input(f"Digite o número {i+1} do primeiro array: "))
        numeros.append(numero)
    for i in range(5):
        numero2=int(input(f"Digite o numero {i+1} do segundo array: "))
        numeros2.append(numero2)
    print("Comparação de valores nas mesmas posições")
    for i in range(len(numeros)):
        if numeros[i]==numeros2[i]:
            print(f"Posição {i}: {numeros[i]} = {numeros2[i]}")
        else:
            print("Não há valores iguais nas mesmas posições ")

if __name__=="__main__":
    comparacao()