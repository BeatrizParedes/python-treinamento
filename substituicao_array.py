"Desenvolva um programa que crie um array de 10 números inteiros. "
"O programa deve pedir ao usuário que forneça dois números:"
"um número para buscar no array e outro para substituir o número encontrado."
"Se o número for encontrado, ele deve ser substituído."

def substituicao():
    numeros=[]
    for i in range(10):
        numero=int(input("Digite o número que deseja inserir: "))
        numeros.append(numero)

    numero_antigo=int(input("Digite o número que deseja buscar: "))
    numero_novo=int(input("Digite o número novo: "))

    encontrado=False
    for i in range(len(numeros)):
        if  numeros[i]==numero_antigo:
            numeros[i]=numero_novo
            encontrado=True
    if encontrado:
        print ("O número foi substituído. Novo array:")
        for numero in numeros:
            print(numero)
    else:
        print("Número não encontrado no array")
    print(numeros)


if __name__=="__main__":
    substituicao()