"Crie um programa que declare um array de 5 números inteiros. Atribua valores a esse array e, em seguida, exiba os valores no console."

def teste_array():
    numeros=[10,20,30,40,50]

    #Exibição dos valores do array
    for i in range(len(numeros)):
        print (f"Elemento {i}: {numeros[i]}")

if __name__=="__main__":
    teste_array()

#O programa cria uma lista com 5 númros inteiros e inicializa seus valores diretamente. 
#Um laço for é usado para percorrer e exibir cada valor da lista