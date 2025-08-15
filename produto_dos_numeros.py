"Crie um programa que calcule o produto dos números inteiros de 1 a 10."

def produto_dos_numeros():
    produto =int(input("Digite o número que deseja multiplicar: "))
    for i in range(1, 11):
        print(f"{produto} x {i} é {produto * i}")
    
if __name__== "__main__":
    produto_dos_numeros()