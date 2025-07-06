"Crie um programa que converta uma temperatura em graus Celsios para Fahreheit"
"A fórmula de conversão é: F =(C*9/5)+32"
"Exiba o resultado no console"

def conversao():
    temperatura = int(input("Escreva a temperatura em Celsius que deseja converter: "))
    conversao = (temperatura*9/5)+32

    print(f"A temperatura {temperatura} convertida para Fahreheit é: {conversao}")

if __name__=="__main__":
    conversao()