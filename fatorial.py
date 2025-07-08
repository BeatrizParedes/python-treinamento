"Desenvolva um programa que calcule o fatorial de um número inteiro fornecido pelo usuário"

def fatorial ():
    escolha=int(input("Escolha um número para saber o fatorial dele: "))
    fatorialdaescolha=1 #A variável não pode ser inicializada em 0 pra funcionar
    for i in range (1,escolha+1): # O programa lê um número inteiro fornecido pelo usuário e 
                                  # utiliza um laço for para multiplicar os números de 1 até o número fornecido, 
                                  # acumulando o resultado na variável fatorial
        fatorialdaescolha*=i
    print(f"Fatorial de {escolha} é: {fatorialdaescolha}")

if __name__=="__main__":
    fatorial()