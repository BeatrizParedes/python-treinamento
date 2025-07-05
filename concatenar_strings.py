"Crie um programa que peça ao usuário para digitar seu nome e sobrenome"
"O programa deve exibir uma mensagem de boas-vindas concatenando o nome e o sobrenome do usuário"

def concatenar():
    nome=input("Poderia informar seu nome? ")
    sobrenome=input("Poderia informar seu sobrenome? ")

    print(f"Seja bem-vindo ao sistema {nome} {sobrenome}")

if __name__ =="__main__":
    concatenar()