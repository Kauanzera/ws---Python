nome = input("Insira seu nome: ")
cidade = input("Sua cidade: ")

try:
    idade = int(input("Sua idade: "))
except ValueError:
    print("Digite um NÚMERO INTEIRO")
    try:
        idade = int(input("Sua idade: "))
    except ValueError:
        print("DIGITE A PORRA DE UM NúMERO INTEIRO CARA")
        idade = int(input("-> "))

try:
    altura = float(input("Sua altura: "))

    if idade >= 18:
        maior = "Maior de idade"
    else:
        maior = "Menor de idade"

    print (f"\nNome = {nome} \nCidade = {cidade} \nIdade = {idade} \nSituação: {maior} \nAltura = {altura}")
except ValueError:
    print("Caracter inválido!")
