print (10 * "--")

def saudacao():
    print ("Olá Mundo!")

saudacao()

print (10 * "--")

def pessoa(nome):
    print (f"Olá {nome}!")

pessoa("Kauan")
pessoa("Mariana")

print (10 * "--")

def chama(a, b):
    return a + b

resultado = chama(7, 11)
print(resultado)

print (10 * "--")

funcao = lambda x: x ** 2       #Cria uma função de uma linha, usando o lambda e declarando o x como o argumento da funcao que retornará o valor de x²
print (funcao(10))

print (10 * "--")

def funcao():
    variavel_local = 10
    print(variavel_local)

variavel_global = 20

def funcao2():
    print (variavel_global)

funcao()
funcao2()
print(variavel_global)
#print(variavel_local)          Retorna um erro por ser uma variavel criada dentro de uma funcao

print (10 * "--")

def somar(a, b):
    print (a + b)

def sub(a, b):
    print (a - b)

def multiplicar(a, b):
    print (a * b)

def divisao(a, b):
    print (a / b)

somar(10, 15)
sub(100, 25)
multiplicar(3, 15)
divisao(100, 10)

print (10 * "--")