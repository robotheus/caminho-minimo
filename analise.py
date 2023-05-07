##ANALISE DOS DADOS
import numpy as np

rede = open("entrada.txt")
linhas = rede.readlines()

#montando o grafo como um dicionario:
grafo = {}

for linha in linhas:
    v1, v2 = linha.split()
        
    if v1 not in grafo:
        grafo[v1] = [v2]
    else:
        grafo[v1].append(v2)
            
    if v2 not in grafo:
        grafo[v2] = [v1]
    else:
        grafo[v2].append(v1)

#aplicando busca em largura no grafo-dicionario
#essa busca em largura recebe um grafo e retorna sua matriz de distancias
visitados = []      #lista dos vertices visitados
fila = []           #lista dos vertices na fila para serem visitados
n = len(grafo)
distancias = np.zeros((n, n))  

def busca_em_largura_com_distancias(grafo):
    n = len(grafo)
    distancias = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        visitados = [False] * n
        fila = []
        
        visitados[i] = True
        fila.append(i)
        distancias[i][i] = 0
        
        while fila:
            vertice = fila.pop(0)
            a = str(vertice)
            x = int(vertice)

            for vizinhos in grafo[a]:
                b = int(vizinhos)
                if not visitados[b]:
                    visitados[b] = True
                    fila.append(vizinhos)
                    distancias[i][b] = distancias[i][x] + 1
    
    return distancias

distancias = busca_em_largura_com_distancias(grafo) #matriz de distancias

#definindo a exentricidade de cada vertice e o diametro do grafo
#a posicao 15 da lista excentricidade diz qual a excentricidad do vertice 15
#a excentricidade de cada vertice é sua maior distancia para outro vertice
#a excentricidade do grafo é a maior excentricidade entre os vertices
excentricidade = []
diametro = 0

for x in range(len(grafo)):
    maior = 0
    
    for y in range(len(grafo)):
        if distancias[x][y] > maior:
            maior = distancias[x][y]
    
    if maior > diametro:
        diametro = maior
    
    excentricidade.append(maior)

#definindo o raio do grafo
raio = excentricidade[0]

for k in excentricidade:
    if k < raio:
        raio = k

centro = []
#definindo o centro da rede:
for i in range(len(excentricidade)):
    if raio == excentricidade[i]:
        centro.append(i)

#definindo a centroide da rede:
m = []
for x in range(len(grafo)):
    d = 0

    for y in range(len(grafo)):
        d += distancias[x][y]

    m.append(d)

centroide = 0
menor = m[0]

for x in range(len(m)):
    if m[x] < menor:
        centroide = x
        menor = m[x]

#definindo os vertices da periferia da rede:
periferia = []

for x in range(len(excentricidade)):
    if excentricidade[x] == diametro:
        periferia.append(x)

#saida dos dados
print("------------------------------------------")
print(f'Excentricidade dos vértices: {excentricidade}')
print("------------------------------------------")
print(f'Diametro da rede: {diametro}')
print("------------------------------------------")
print(f'Raio da rede: {raio}')
print("------------------------------------------")
print(f'Vertices do centro da rede: {centro}')
print("------------------------------------------")
print(f'Vertice centroide da rede: {centroide}')
print("------------------------------------------")
print(f'Vertices da periferia da rede: {periferia}')
print("------------------------------------------")

for x in distancias:
    print(x)
    