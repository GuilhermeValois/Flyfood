from cidade import Cidade
import sys
import time

ponto_inicial = None
cidades = []

#Obtenção da matriz
print("Digite o tamanho da matris(Ex:4x5) e a matriz (Linha por linha):\n")
matriz = sys.stdin.read().split()
#Separando o dado de tamanho da matriz da matriz em si
tamanho_matriz = matriz[0]
matriz = matriz[1:]
#Definindo a quantidade de linhas e colunas da matriz inicialmente ajustadas para 0
linhas = 0
colunas = 0
for algarismo in tamanho_matriz:
    if algarismo == "x" or algarismo == "X":
        linhas = int(tamanho_matriz[:tamanho_matriz.index(algarismo)])
        colunas = int(tamanho_matriz[tamanho_matriz.index(algarismo)+1:])
#Obtendo o ponto inicial e a posição das cidades na matriz
linha = 0
coluna = 0
while linha < linhas:
    linha_escolhida = matriz[linha] 
    while coluna < colunas:
        if linha_escolhida[coluna] in "rR":
            ponto_inicial = Cidade("R",linha,coluna)
            #ponto_inicial = (linha_escolhida[coluna],linha, coluna)
        elif linha_escolhida[coluna].isalpha():
            cidade_a = Cidade(linha_escolhida[coluna],linha,coluna)
            cidades.append(cidade_a)
            #cidades.append((linha_escolhida[coluna],linha,coluna))
        coluna += 1
    coluna = 0
    linha += 1

inicio = time.perf_counter()

combinacoes = []
combinacao = []

def combinar_cidades(cidades,combinacao):
    """
    Função que gera todas as possibilidades de caminhos
    entre as cidades guardando as combinações em uma lista
    """
    for cidade in cidades:
        
        if cidade not in combinacao:
            combinacao.append(cidade)
            
            if len(combinacao) < len(cidades):
                combinar_cidades(cidades,combinacao)
                
                combinacao.pop()
            else:
                combinacoes.append(combinacao.copy())
                combinacao.pop()

combinar_cidades(cidades,combinacao)
#Registrando em uma lista cada caminho a sua distância calculada
distancias = []

for combinacao in combinacoes:
    distancia_total = 0
    for indice in range(0,len(combinacao)-1): 
        distancia_y = abs(combinacao[indice].linha - combinacao[indice+1].linha)
        distancia_x = abs(combinacao[indice].coluna - combinacao[indice+1].coluna)
        distancia_total += distancia_y+distancia_x

    distancia_y = abs(ponto_inicial.linha - combinacao[0].linha)
    distancia_x = abs(ponto_inicial.coluna - combinacao[0].coluna)
    distancia_total += distancia_y+distancia_x

    distancia_y = abs(ponto_inicial.linha - combinacao[-1].linha)
    distancia_x = abs(ponto_inicial.coluna - combinacao[-1].coluna)
    distancia_total += distancia_y+distancia_x

    distancias.append((combinacao,distancia_total))

#Procurando o menor caminho
menor_caminho = distancias[0]
for caminho in distancias:
    if menor_caminho[1] > caminho[1]:
        menor_caminho = caminho
fim = time.perf_counter()
#Imprimindo o menor caminho e sua distância
print(f"Menor caminho:{menor_caminho}")
print(f"Tempo do algoritmo: {fim - inicio:.4f} segundos")
                    