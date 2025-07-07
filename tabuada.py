"Crie um programa que exiba a tabuada de um número fornecido pelo usuário, de 1 a 10"

def tabuada():
    escolha=int(input("Escolha um número para saber a tabuada: "))
    for i in range (1, 11):
        print(f"{escolha} x {i} = {escolha*i}")
if __name__=="__main__":
    tabuada()