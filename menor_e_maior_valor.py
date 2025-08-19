"Desenvolva um programa que leia 10 números inteiros e armazene-os em um array."
"Encontre e exiba o menor e o maior valor presentes no array"

def menor_e_maior():
    numeros=[]

    for i in range(10):
        numero=int(input(f"Digite o numero {i+1} "))
        numeros.append(numero)
    
    maior=menor=numeros[0] #Esse parâmetro precisa ser passado aqui para que não dê erro com a lista de números

    for numero in numeros:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero
    
    print(f"O maior número é o {maior}")
    print(f"O menor número é o {menor}")

if __name__== "__main__":
    menor_e_maior()