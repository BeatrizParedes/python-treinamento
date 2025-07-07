"Escreva um programa que calcule a soma de todos os numeros de 1 a 100"

def soma():
    soma=0
    for i in range (1,101):
        soma+=i
    print(f"Soma de 1 a 100: {soma}")
if __name__=="__main__":
    soma()