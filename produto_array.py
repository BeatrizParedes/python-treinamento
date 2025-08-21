"Crie um programa que leia 6 números inteiros e calcule o produto de todos os valores do array."

def produtos():
    numeros=[]
    produto=1
    for i in range (6):
        numero=int(input(f"Digita o número {i+1}: "))
        numeros.append(numero)
        produto*=numero #é equivalente a produto = produto * numero
    print(f"O produto dos numeros é: {produto}")

if __name__=="__main__":
    produtos()