"Escreva um programa que leia 15 números inteiros e, em seguida, exiba quantos desses números são positivos e quantos são negativos"

def posi_neg():
    numeros=[]
    positivos=negativos=0

    for i in range (15):
        resto=15-i
        numero=(int(input(f"Digite o número {i+1} (restam {resto}): ")))
        numeros.append(numero)

    for numero in numeros:
        if numero>0:
            positivos+=1
        elif numero<0:
            negativos+=1
    
    print(f"A quantidade de números positivos é: {positivos}")
    print(f"A quantidade de números negativos é: {negativos}")
            
if __name__=="__main__":
    posi_neg()