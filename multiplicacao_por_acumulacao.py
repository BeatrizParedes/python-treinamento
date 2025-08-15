"Desenvolva um programa que leia um número e multiplique esse número por 2 repetidamente até o valor exceder 1000."

def multiplicacao_por_acumulacao():
    num=int(input("Digite um número: "))
    while num <= 1000:
        print(num)
        num *=2

if __name__=="__main__":
    multiplicacao_por_acumulacao()