"Desenvolva um programa que leia números inteiros do usuário, um por vez, e acumule a soma deles usando o operador de atribuição +="
"Dica: Utilize o Scanner para pedir os dados, e você pode utilizar um loop for para repetir a solicitação de dados 5 vezes"

def acumulacao():
    soma_acumulada=0
    for i in range(1,6):
        valor_digitado=int(input(f"Escreva o {i}º número inteiro: "))
        soma_acumulada += valor_digitado

        print(f"Soma acumulada: {soma_acumulada}")

if __name__=="__main__":
    acumulacao()