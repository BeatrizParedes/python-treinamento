"Escreva um programa que some todos os números pares de 1 a 100 e, separadamente, todos os números ímpares de 1 a 100."

def soma_pares_impares():
    soma_pares=0
    soma_impares=0

    for i in range(1, 101):
        if i%2==0:
            soma_pares+=1
        else:
            soma_impares+=1
    
    print(f"A soma dos números pares de 1 a 100 é {soma_pares}")
    print(f"A soma dos números ímpares de 1 a 100 é {soma_impares}")
    
if __name__ =="__main__":
    soma_pares_impares()