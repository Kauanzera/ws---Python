try:                                     #usado pra tratar erros de compilação ou lógica
    resultado = 10
    div = resultado / 0
    print (div)
except ZeroDivisionError:       
    print ("Erro: Divisor Zero")
except ValueError:
    print ("Erro: Valor Errado")

try:
    arquivo = open("arquivo.txt", "r")      #abre o arquivo descrito
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
"""finally:
    arquivo.close()"""                         #Fecha o arquivo aberto, independente se dado o erro ou não

def funcao():
    if condicao:
        raise Exception ("Descrição do Erro")       #Tratamento de erros personalizado

try:
    funcao()
except Exception as e:
    print (f"Tem algo errado: {str(e)}")                #Imprimirá o erro personalizado junto do 
                                                        # erro da linguagem python: "Tem algo errado: name 'condicao' is not defined"