"Dica arrays multidimensionais podem ser criados utilizando a sintaxe: int[][]x=[2][2], sendo assim este array terá 2 linhas e 2 colunas."
"Crie um programa que declare uma matriz 3x3 e permita que o usuário insira valores inteiros para preencher essa matriz."
"Em seguida, exiba os valores da matriz no console."

def matriz():
    matriz=[[0 for _ in range(3)]for _ in range (3)] #Cria uma lista, colocando o número 0 para cada vez que eu passo pelo range(3). O _ é só um nome de variável descartável - usamos _ por que não precisamos do valor, só queremos repetir. O range(3) gera a sequência 0,1,2(três elementos)
    for i in range(3):
        for j in range(3):
            matriz[i][j]=int(input(f"Digite o valor para a posição[{i}][{j}]:"))
    print("\nMatriz 3x3:")
    for linha in matriz:
        print("".join(map(str,linha)))  # O print só consegue juntar direto coisas que já são strings
                                        # map(str,linha) Pega cada número da lista e transforma em texto.
if __name__=="__main__":                # "".join(...) Junta todos os elementos dessa lista de textos
    matriz()