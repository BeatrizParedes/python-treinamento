"Escreva um programa que leia as idades de duas pessoas e exiba quem é mais velho."
"Caso as idades sejam iguais, exiba uma mensagem informando que as uas pessoas têm a mesma idade"

def idades():
    idade1=int(input("Escreva a primeira idade: "))
    idade2=int(input("Escreva a segunda idade: "))

    if (idade1>idade2):
        print(f"O individuo com {idade1} é o mais velho")
    elif (idade2>idade1):
        print(f"O individuo com {idade2} é o mais velho")
    else:
        print("Eles possuem a mesma idade")

if __name__=="__main__":
    idades()