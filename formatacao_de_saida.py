"Desenvolva um programa que exiba o valor de uma variável double com duas casas decimais."
"Utilize formatação para garantir que o valor seja exibido corretamente"

def formatacao():

    valor = 1212323231.2323231
    print(f"Valor formatado:{valor:.2f}") #Exibe o valor com duas casas decimais

if __name__ == "__main__":
    formatacao()