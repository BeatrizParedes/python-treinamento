"Desenvolva um programa que leia a largura e a altura de um retângulo e calcule a área no console"
"Dica: area = largura x altura"

def area_retangulo():
    largura = int(input("Escreva a largura do retângulo: "))
    altura = int(input("Escreva a altura do retângulo: "))
    area = largura*altura

    print(f"A área do retângulo que possui {largura} de largura e {altura} de altura é: ",area)

if __name__=="__main__":
    area_retangulo()