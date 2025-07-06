"Crie um programa que leia dois números inteiros e exiba se o primeiro é maior, menor ou igual ao segundo"

def comparacao():
    num1= int(input("Insira o número 1: "))
    num2= int(input("Insira o número 2: "))
    
    if(num1>num2):
        print(f"O número {num1} é maior que o {num2}")
    elif(num1==num2):
        print(f"O número {num1} é igual a {num2}")
    else:
        print(f"O número {num1} é menor que o {num2}")
        
if __name__=="__main__":
    comparacao()