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

def tendencia_missao(pontos_ciclos):
    if pontos_ciclos[0] > pontos_ciclos[-1]:
        return 'A missão apresentou tendência de piora.'
    elif pontos_ciclos[0] < pontos_ciclos[-1]:
        return 'A missão apresentou tendência de melhora.'
    else:
        return 'A missão permaneceu estável em relação ao início.'

def identificar_area_mais_afetada(pontos_dados_ciclos):
    pontos_total_temp = 0
    pontos_total_comunicacao = 0
    pontos_total_bateria = 0
    pontos_total_oxigenio = 0
    pontos_total_estabilidade = 0

    for dado in pontos_dados_ciclos:
        pontos_total_temp += dado[0]
        pontos_total_comunicacao += dado[1]
        pontos_total_bateria += dado[2]
        pontos_total_oxigenio += dado[3]
        pontos_total_estabilidade += dado[4]
    
    mapeamento_areas = {
        'Temperatura interna': pontos_total_temp,
        'Comunicação com a base': pontos_total_comunicacao,
        'Sistema de energia': pontos_total_bateria,
        'Suporte de oxigênio': pontos_total_oxigenio,
        'Estabilidade operacional': pontos_total_estabilidade
    }
    
    area_mais_afetada = max(mapeamento_areas, key=mapeamento_areas.get)
    maior_valor = mapeamento_areas[area_mais_afetada]

    match area_mais_afetada:
        case 'Temperatura interna':
            recomendacao_automatica = 'Ativar radiadores suplementares e reorientar defletores térmicos contra irradiação.'
        case 'Comunicação com a base':
            recomendacao_automatica = 'Iniciar varredura de frequência de backup e realinhar antena de alto ganho com a DSN.'
        case 'Sistema de energia':
            recomendacao_automatica = 'Modo de Sobrevivência Ativo: Desligar subsistemas científicos e priorizar aquecedores de bateria.'
        case 'Suporte de oxigênio':
            recomendacao_automatica = 'Isolar vazamentos nas linhas de pressurização e acionar tanques criogênicos de reserva.'
        case 'Estabilidade operacional':
            recomendacao_automatica = 'Interromper perfuração mecânica e calibrar giroscópios do sistema de atitude (RCS).'
    
    return area_mais_afetada, maior_valor, recomendacao_automatica, pontos_total_temp, pontos_total_comunicacao, pontos_bateria, pontos_total_oxigenio, pontos_total_estabilidade

fases_missao = [
    "Lançamento Interplanetário",
    "Assistência Gravitacional de Marte",
    "Cruzeiro Profundo e Teste Óptico",
    "Chegada e Captura Órbita A",
    "Descida para Órbita B",
    "Lançamento de Microssondas de Impacto",
    "Preparação para o Pouso Experimental",
    "Descida Autônoma de Baixa Altitude",
    "Fixação Magnética/Mecânica",
    "Análise Direta in loco",
    "Curto-circuito (Alta temp, drena energia, afeta oxigênio e estabilidade)",
    "Isolamento da falha e acionamento dos sistemas de backup",
    "Ativação da Estação Permanente"
]

ciclo_mais_critico = -1
maior_pontuacao = 0
def identificar_ciclo_mais_critico():
    for ciclo in pontos_ciclos:    
        if pontos_ciclos[ciclo] > ciclo_mais_critico:
            ciclo_mais_critico = ciclo
            maior_pontuacao = pontos_ciclos[ciclo]
        else:
            continue
    return ciclo_mais_critico, maior_pontuacao

risco_medio = 0
soma_pontos_ciclos = 0
def calcular_risco_medio():
    for ciclo in pontos_ciclos:
        soma_pontos_ciclos += pontos_ciclos[ciclo]
    risco_medio = soma_pontos_ciclos / len(pontos_ciclos)
    return risco_medio

qnt_ciclos_criticos = 0
qnt_ciclos_atencao = 0
qnt_ciclos_normal = 0
def calcular_qnt_ciclos_criticos():
    for ciclo in classificacao_ciclos:
        if classificacao_ciclos[ciclo] == 'MISSÃO CRÍTICA':
            qnt_ciclos_criticos += 1
        elif classificacao_ciclos[ciclo] == 'MISSÃO ESTÁVEL':
            qnt_ciclos_atencao += 1
        else:
            qnt_ciclos_normal += 1
        
    if qnt_ciclos_normal > qnt_ciclos_atencao and qnt_ciclos_normal > qnt_ciclos_criticos:
        classificacao_missao = 'MISSÃO NORMAL'
    elif qnt_ciclos_atencao > qnt_ciclos_normal and qnt_ciclos_atencao > qnt_ciclos_criticos:
        classificacao_missao = 'MISSÃO ESTÁVEL'
    else:
        classificacao_missao = 'MISSÃO CRÍTICA'

    return qnt_ciclos_criticos, classificacao_missao

cont = 0
media_temp = 0
media_comunicacao = 0
media_bateria = 0
media_oxigenio = 0
media_estabilidade = 0
soma_temp = 0
soma_comunicacao = 0
soma_bateria = 0
soma_oxigenio = 0
soma_estabilidade = 0
for i in dados_missao:
    soma_temp += i[0]
    soma_comunicacao += i[1]
    soma_bateria += i[2]
    soma_oxigenio += i[3]
    soma_estabilidade += i[4]
    cont += 1

media_temp = soma_temp / cont
media_comunicacao = soma_comunicacao / cont
media_bateria = soma_bateria / cont
media_oxigenio = soma_oxigenio / cont
media_estabilidade = soma_estabilidade / cont

def relatorio_final():
    print(f'{'='}*20')
    print('𝗠𝗜𝗦𝗦𝗜𝗢𝗡 𝗖𝗢𝗡𝗧𝗥𝗢𝗟 𝗔𝗜')
    print(f'{'='}*20')
    print('Missão: Core Horizon X')
    print('Equipe: Equipe PAD Dynamics')
    print('Quantidade de cilos analisados: 13')
    print(f'{'='}*20\n')
    for i in range(len(dados_missao)):
        print(f'\nCICLO {i + 1} — {fases_missao[i]}')
        print('-' * 40)
        print(f'Temperatura:  {dados_missao[i][0]}°C | {classificacao_ciclos[i][0]} | {pontos_dados_ciclos[i][0]} pts')
        print(f'Comunicação:  {dados_missao[i][1]}%  | {classificacao_ciclos[i][1]} | {pontos_dados_ciclos[i][1]} pts')
        print(f'Bateria:      {dados_missao[i][2]}%  | {classificacao_ciclos[i][2]} | {pontos_dados_ciclos[i][2]} pts')
        print(f'Oxigênio:     {dados_missao[i][3]}%  | {classificacao_ciclos[i][3]} | {pontos_dados_ciclos[i][3]} pts')
        print(f'Estabilidade: {dados_missao[i][4]}%  | {classificacao_ciclos[i][4]} | {pontos_dados_ciclos[i][4]} pts')
        print(f'PONTUAÇÃO TOTAL DO CICLO: {pontos_ciclos[i]} pontos')
        print(f'CLASSIFICAÇÃO TOTAL DO CICLO: {classificacao_ciclos[i]}')
    print('=' * 40)
    print('RELATORIO FINAL DA MISSÃO')
    print('=' * 40)
    print('Missão: Core Horizon X')
    print('Equipe: Equipe PAD Dynamics')
    print('Quantidade de cilos analisados: 13\n')
    print(f'Média de Temperatura:  {media_temp:.2f}°C')
    print(f'Média de Comunicação:  {media_temp:.2f}%')
    print(f'Média de Bateria:      {media_temp:.2f}%')
    print(f'Média de Oxigênio:     {media_temp:.2f}%')
    print(f'Média de Estabilidade: {media_temp:.2f}%\n')
    print(f'Ciclo mais crítico: {ciclo_mais_critico}')
    print(f'Maior pontuação de risco: {maior_pontuacao}')
    print(f'Risco Médio da missão: {risco_medio}')
    print(f'Quantidade de ciclos críticos: {qnt_ciclos_criticos}\n')
    print(f'Tendência de missão: {tendencia_missao(pontos_ciclos)} \n')
    print('Pontuação acumulada por área: ')
    print(f'Temperatura interna->  {pontos_total_temp}')
    print(f'Comunicação com a base-> {pontos_total_comunicacao}')
    print(f'Sistema de energia-> {pontos_total_bateria}')
    print(f'Suporte de oxigênio-> {pontos_total_oxigenio}')
    print(f'Estabilidade operaional-> {pontos_total_estabilidade}\n')
    print(f'Área mais afetada: {area_mais_afetada}\n')
    print(f'CLassificação final da missão: {classificacao_missao}')
    print('=' * 40)    