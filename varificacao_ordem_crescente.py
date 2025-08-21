"Escreva um programa que leia 8 números inteiros e verifique se os valores estão em ordem crescente."
"Exiba uma mensagem indicando se os números estão ou não em ordem"

def ordenador():
    numeros=[]
    em_ordem=True
    for i in range (8):
        numero=int(input(f"Digite o número {i+1}: "))
        numeros.append(numero)
    for i in range(len(numeros)-1):
        if numeros[i]>numeros[i+1]:
            em_ordem=False
            break
    if em_ordem:
        print("Os números estão em ordem crescente.")
    else:
        print("Os números NÃO estão em ordem crescente.")

if __name__=="__main__":
    ordenador()