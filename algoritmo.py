
def calcular_distancia(combinacao,ponto_inicial):
    """
    Função que calcula a distância entre as cidades de uma determinada combinação, 
    considerando o ponto inicial como ponto de partida e chegada
    """
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

    
    return (combinacao.copy(),distancia_total)




def combinar_cidades(cidades,combinacao,combinacoes,ponto_inicial):
    """
    Função que gera todas as possibilidades de caminhos
    entre as cidades, calcula a distância e seleciona a
    sequência de cidades com o menor caminho
    """
    for cidade in cidades:
        
        if cidade not in combinacao:
            combinacao.append(cidade)
            
            if len(combinacao) < len(cidades):
                combinar_cidades(cidades,combinacao,combinacoes,ponto_inicial)
                
                combinacao.pop()
            else:
                caminho = calcular_distancia(combinacao,ponto_inicial)
                if combinacoes == []:
                    combinacoes.append(caminho)
                elif caminho[1] < combinacoes[0][1]:
                    combinacoes.clear()
                    combinacoes.append(caminho)
                        
                elif caminho[1] == combinacoes[0][1] and caminho not in combinacoes:
                    combinacoes.append(caminho)
                
                combinacao.pop()