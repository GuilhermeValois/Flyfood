from cidade import Cidade
import os
import time
import algoritmo


ponto_inicial = None
cidades = []

#Obtenção da matriz do arquivo txt
caminho_entrada = os.path.join(os.path.dirname(__file__), "entrada.txt")

caso_escolhido = 4

with open(caminho_entrada, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

caso_atual = 0
entrada = []

dentro_do_caso = False

for linha in linhas:
    linha = linha.strip()

    if linha.startswith("CASO"):
        caso_atual = int(linha.split()[1])
        dentro_do_caso = caso_atual == caso_escolhido

    elif linha == "FIM":
        dentro_do_caso = False

    elif dentro_do_caso and not linha.startswith("CASO"):
        entrada.append(linha)

matriz_de_entrada = []

for linha in entrada:
    matriz_de_entrada.extend(linha.split())

#Definindo a quantidade de linhas e colunas da matriz
linhas = int(matriz_de_entrada[0])
colunas = int(matriz_de_entrada[1])

#Separando o dado de tamanho da própria matriz matriz
matriz = matriz_de_entrada[2:]

#Tratando a matriz para que seja possível acessar cada elemento de forma mais simples
linha = 0
coluna = 0
index = 0
matriz_tratada = []
while linha < linhas:
    lista_linhas = []
    while coluna < colunas:
        lista_linhas.append(matriz[index])
        index += 1
        coluna += 1
    matriz_tratada.append(lista_linhas)
    coluna = 0
    linha += 1

#Obtendo o ponto inicial e a posição das cidades na matriz
linha = 0
coluna = 0
while linha < linhas:
    linha_escolhida = matriz_tratada[linha] 
    while coluna < colunas:
        if linha_escolhida[coluna] in "rR":
            ponto_inicial = Cidade("R",linha,coluna)
        elif linha_escolhida[coluna].isalpha():
            cidade_a = Cidade(linha_escolhida[coluna],linha,coluna)
            cidades.append(cidade_a)
        coluna += 1
    coluna = 0
    linha += 1

#Iniciando a lista das combinações e a lista de uma combinação de cidades, que será preenchida recursivamente
combinacoes = []
combinacao = []

#Execução do algoritmo de combinação de cidades e cálculo da distância, marcando seu tempo de execução
inicio = time.perf_counter()

algoritmo.combinar_cidades(cidades,combinacao,combinacoes,ponto_inicial)

fim = time.perf_counter()

#Imprimindo o menor caminho e sua distância
print(f"Menor caminho:{'->'.join(cidade.nome for cidade in combinacoes[0][0])} com distância de {combinacoes[0][1]} dronômetros")
print(f"Caminhos de mesma distância: {combinacoes[1:]}")
print(f"Tempo do algoritmo: {fim - inicio:.4f} segundos")