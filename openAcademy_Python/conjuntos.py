#Para criar um conjunto em Python, deve-se usar {} e os valores dentro, ou o método set([]) e os valores dentro.

frutas = {"Maçã", "Banana", "Pêssego", "Uva"}   #Criação de Conjuntos
numeros = set([1, 2, 3, 4, 5])                  #Criação de Conjuntos

conjunto_1 = {1, 2, 3}      #Criação de Conjuntos
conjunto_2 = {3, 4, 5}   #Criação de Conjuntos

uniao = conjunto_1 | conjunto_2 #Junta as duas variáveis
print (f"União -> {uniao}")

intersecao = conjunto_1 & conjunto_2    #Separa e guarda somente o valor que existe nas duas variáveis
print (f"Interseção -> {intersecao}")

diferenca = conjunto_1 - conjunto_2     #Separa os números do conjunto_1 que não existem no conjunto_2
print (f"Diferença 1 -> {diferenca}")

diferenca2 = conjunto_2 - conjunto_1
print (f"Diferença 2 -> {diferenca2}")

diferenca_simetrica = conjunto_1 ^ conjunto_2       #Separa os números que são diferentes nos dois conjuntos
print (f"Diferença Simétrica -> {diferenca_simetrica}")


#Métodos de conjuntos.

carros = {"Bugatti", "Masserati", "Ferrari"}
print (f"CARROS -> {carros}")

carros.add("Mercedes")      #Adiciona o valor "Mercedes" ao conjunto
print (f".ADD -> {carros}")

carros.remove("Masserati")          #Remove o valor "Masserati" do conjunto, se o valor não existir no conjunto, retorna um erro
print (f".REMOVE -> {carros}")

carros.discard("Tesla")             #Remove o valor "Tesla" do conjunto, se o valor não existir, ele não retorna erro e segue o código
print (f".DISCARD -> {carros}")

carros.clear()                      #Limpa o conjunto inteiro
print (f".CLEAR -> {carros}")
