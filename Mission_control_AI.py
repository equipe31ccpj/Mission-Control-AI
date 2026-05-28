# Monitoramento de Missão: 16 Psyche (Coração Metálico)
# Ciclo 1 — Lançamento Interplanetário
# Ciclo 2 — Assistência Gravitacional de Marte
# Ciclo 3 — Cruzeiro Profundo e Teste Óptico
# Ciclo 4 — Chegada e Captura Órbita A
# Ciclo 5 — Descida para Órbita B
# Ciclo 6 — Lançamento de Microssondas de Impacto
# Ciclo 7 — Preparação para o Pouso Experimental
# Ciclo 8 — Descida Autônoma de Baixa Altitude
# Ciclo 9 — Fixação Magnética/Mecânica
# Ciclo 10 — Análise Direta in loco
# Ciclo 11 — Curto-circuito (Alta temp, drena energia, afeta oxigênio e estabilidade)
# Ciclo 12 — Isolamento da falha e acionamento dos sistemas de backup
# Ciclo 13 — Ativação da Estação Permanente 

dados_missao = [
    [22, 98, 100, 100, 100], 
    [25, 95, 100, 100,  98],  
    [18, 90, 98,  99,   95],  
    [24, 85, 82,  95,   90],  
    [24, 15, 80,  95,   30],  
    [25, 80, 84,  94,   92], 
    [26, 88, 80,  94,   95], 
    [12, 60, 62,  90,   85],  
    [17, 40, 49,  85,   70],    
    [25, 75, 67,  85,   88],  
    [36, 20, 41,  50,   40], 
    [28, 78, 43,  90,   85],  
    [22, 77, 63,  79,   75]   
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

def monitorar_temp(temp_atual):
    if temp_atual > 32 or temp_atual < 10:
        return 'CRÍTICO', 2
    elif 18 <= temp_atual <= 26:
        return 'NORMAL', 0
    else:
        return 'ATENÇÂO', 1
    
def monitorar_comunicacao(comunicacao_atual):
    if comunicacao_atual > 69:
        return 'NORMAL', 0
    elif comunicacao_atual < 35:
        return 'CRÍTICO', 2
    else:
        return 'ATENÇÂO', 1

def monitorar_bateria(bateria_atual):
    if bateria_atual > 59:
        return 'NORMAL', 0
    elif bateria_atual < 30:
        return 'CRÍTICO', 2   
    else:
        return 'ATENÇÂO', 1
    
def monitorar_oxigenio(oxigenio_atual):
    if oxigenio_atual > 79:
        return 'NORMAL', 0
    elif oxigenio_atual < 40:
        return 'CRÍTICO', 2
    else:
        return 'ATENÇÂO', 1
        
def monitorar_estabilidade(estabilidade_atual):
    if estabilidade_atual > 74:
        return 'NORMAL', 0
    elif estabilidade_atual < 50:
        return 'CRÍTICO', 2
    else:
        return 'ATENÇÂO', 1

classificacoes_dados_ciclos = []
pontos_dados_ciclos = []
pontos_ciclos = []
classificacao_ciclos = [] 
for ciclo in dados_missao:
    status_temp, pontos_temp = monitorar_temp(ciclo[0])
    status_comunicacao, pontos_comunicacao = monitorar_comunicacao(ciclo[1])
    status_bateria, pontos_bateria = monitorar_bateria(ciclo[2])
    status_oxigenio, pontos_oxigenio = monitorar_oxigenio(ciclo[3])
    status_estabilidade, pontos_estabilidade = monitorar_estabilidade(ciclo[4])
    pontuacao_ciclo = pontos_temp + pontos_comunicacao + pontos_bateria + pontos_oxigenio + pontos_estabilidade 
    if pontuacao_ciclo >= 6:
        classificacao_ciclo = 'MISSÃO CRÍTICA'
    elif pontuacao_ciclo <= 2:
        classificacao_ciclo = 'MISSÃO ESTÁVEL'
    else:
        classificacao_ciclo = 'MISSÃO EM ATENÇÃO'

    classificacoes_dados_ciclos.append([status_temp, status_comunicacao, status_bateria, status_oxigenio, status_estabilidade])
    pontos_dados_ciclos.append([pontos_temp, pontos_comunicacao, pontos_bateria, pontos_oxigenio, pontos_estabilidade])
    pontos_ciclos.append(pontuacao_ciclo)
    classificacao_ciclos.append(classificacao_ciclo)

