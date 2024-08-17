arquivo = open("dados.txt", "r")        #Abre o arquivo 
conteudo = arquivo.read         #Lê o conteúdo do arquivo
print (conteudo)        #Imprime o conteúdo do arquivo
arquivo.close       #Fecha o arquivo IMPORTANTE