###TRATAMENTO DOS DADOS OBTIDOS EM http://www-personal.umich.edu/~mejn/netdata/dolphins.zip
import re

gml = open("dolphins.gml")
grafo_list = list(gml)

entrada = open("entrada.txt", "w")

i = 0
for busca in grafo_list:
    if ("source" in busca) or ("target" in busca):
        string = ''.join(re.findall('\d+', busca))
        entrada.write(string)
        entrada.write("\t")
        i += 1
        if i == 2:
            entrada.write("\n")
            i = 0

gml.close()