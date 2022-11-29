#manipulando arquivos
#Função open
# "variavel = open(nome, modo)
#
#modos:
# r = somente leitura
# w = escrita(se arquivo já existe, ele apaga e cria um novo vazio)
# a = leitura e escrita (Adiciona    novo conteúdo ao arquivo )
# r+ = leitura e escrita
# w+ = leitura (igual a w)
# a+ = leitura e escrita (Atualização)
#=====================================================================

# arquivo = open("teste1.txt")
#
# texto = arquivo.read()
# print(texto)

file = open("teste2.txt", "a")

file.write("Esse eh meu segundo teste em arquivos")

file.close()



