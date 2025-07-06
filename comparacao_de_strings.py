"Desenvolva um programa que leia duas strings do usuário e verifique se elas são iguais."
"Exiba uma mensagem informando o resultado da comparação"

def comparacao():
    nome1=input("Escreva o primeiro nome: ")
    nome2=input("Escreva o segundo nome: ")

    if(nome1==nome2):
        print("Os nomes são iguais")
    else:
        print("Os nomes são diferentes")

if __name__=="__main__":
    comparacao()