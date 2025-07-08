"Crie um programa que leia 5 números inteiros do usuário e calcule a média deles"

def media():
    soma=0
    for i in range (1,6):
        numero=int(input(f"Escolha o {i}º número: "))
        soma+=numero
    print(f"A média dos números informados é: {soma/5}") #O print deve estar na mesma linha do for
if __name__=="__main__":
    media()