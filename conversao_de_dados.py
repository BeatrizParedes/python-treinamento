"Escreva um programa que converta um valor float em int e outro valor int em float. "
"Exiba os resultados das conversões e explique a diferença entre conversão explícita e implícita. "

def conversao_tipos():
    valor_float = 9.99
    valor_int = int(valor_float) #Conversão explícita de float para int (trunca o valor decimal, ou seja, a parte decimal é descartada)
    print(valor_int)

    numero = 10
    numero_convertido = float(numero) #Conversão implícita de int para float. 
                                      #Em Python, essa conversão ocorre automaticamente durante operações que envolvem tipos mistos, sem perda de informação
    print ("Valor convertido para int", numero_convertido)

if __name__ == "__main__":
    conversao_tipos()