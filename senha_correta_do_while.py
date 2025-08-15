"Escreva um programa que peça ao usuário para digitar uma senha. Continue pedindo a senha até que a senha correta seja digitada."

def senha_correta():
    
    senha_correta="python"
    senha_digitada=""

    while senha_digitada != senha_correta:
        senha_digitada=input("Digite a senha: ")
        if senha_digitada != senha_correta:
            print("Senha incorreta. Tente novamente.")

    print("Senha correta! Acesso concedido.")

if __name__ == "__main__":
    senha_correta()