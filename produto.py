"Crie um programa que calcule o produto dos números inteiros de 1 a 10."

def produto():
    num1 = 1
    for i in range (1, 11):
        num1*=i

    print(f"O produto dos números de 1 a 10 é {num1}")
    
if __name__=="__main__":
    produto()