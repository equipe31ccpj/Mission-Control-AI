# Mission Control AI — Core Horizon X

O **Mission Control AI** é um sistema inteligente baseado em regras lógicas desenvolvido em Python para o monitoramento automatizado e contínuo de missões aeroespaciais. O software analisa telemetrias críticas distribuídas em ciclos operacionais, calcula matrizes de risco, identifica tendências de integridade da espaçonave e gera recomendações de contingência automáticas para apoiar a tomada de decisões.

---

## 🚀 Estrutura do Projeto

O sistema foi modelado para acompanhar a missão **Core Horizon X** ao longo de 13 fases operacionais distintas (desde o lançamento até a ativação da estação permanente). 

Em cada ciclo, as seguintes variáveis são processadas:
1. **Temperatura Interna** (em °C)
2. **Comunicação com a Base** (Qualidade do sinal, em %)
3. **Sistema de Energia** (Nível de bateria, em %)
4. **Suporte de Oxigênio** (Disponibilidade, em %)
5. **Estabilidade Operacional** (Métrica geral do sistema, em %)

---

## 📊 Regras de Alerta e Customização de Limites

Conforme permitido pelas diretrizes do projeto, os limites operacionais foram calibrados e refinados pela equipe **PAD Dynamics** para refletir cenários mais estritos de segurança espacial.

### 🌡️ Temperatura Interna
| Condição | Classificação | Pontuação |
| :--- | :---: | :---: |
| Menor que 10°C | **CRÍTICO** | 2 pts |
| De 11°C até 17°C | **ATENÇÃO** | 1 pt |
| De 18°C até 26°C | **NORMAL** | 0 pts |
| De 27°C até 32°C | **ATENÇÃO** | 1 pt |
| Maior que 32°C | **CRÍTICO** | 2 pts |

### 📡 Comunicação com a Base
| Condição | Classificação | Pontuação |
| :--- | :---: | :---: |
| Maior que 69% | **NORMAL** | 0 pts |
| De 35% até 69% | **ATENÇÃO** | 1 pt |
| Menor que 35% | **CRÍTICO** | 2 pts |

### 🔋 Sistema de Energia (Bateria)
| Condição | Classificação | Pontuação |
| :--- | :---: | :---: |
| Maior que 59% | **NORMAL** | 0 pts |
| De 30% até 59% | **ATENÇÃO** | 1 pt |
| Menor que 30% | **CRÍTICO** | 2 pts |

### 🌬️ Suporte de Oxigênio
| Condição | Classificação | Pontuação |
| :--- | :---: | :---: |
| Maior que 79% | **NORMAL** | 0 pts |
| De 40% até 79% | **ATENÇÃO** | 1 pt |
| Menor que 40% | **CRÍTICO** | 2 pts |

### ⚖️ Estabilidade Operacional
| Condição | Classificação | Pontuação |
| :--- | :---: | :---: |
| Maior que 74% | **NORMAL** | 0 pts |
| De 50% até 74% | **ATENÇÃO** | 1 pt |
| Menor que 50% | **CRÍTICO** | 2 pts |

---

## 🧠 Lógica de Análise e Inteligência do Sistema

A inteligência do software opera de forma estritamente determinística através de estruturas condicionais aninhadas e processamento matricial:

1. **Pontuação do Ciclo:** Cada variável é avaliada individualmente pelas funções de monitoramento. O somatório de pontos do ciclo varia de `0` (estabilidade total) a `10` (criticidade máxima).
2. **Classificação do Ciclo:** - **0 a 2 pontos:** `MISSÃO ESTÁVEL`
   - **3 a 5 pontos:** `MISSÃO EM ATENÇÃO`
   - **6 a 10 pontos:** `MISSÃO CRÍTICA`
3. **Análise de Tendência:** O algoritmo compara analiticamente o risco aritmético do primeiro ciclo com o do último ciclo, determinando se a operação apresenta tendência de *melhora*, *piora* ou *estabilidade*.
4. **Área Mais Afetada e Motor de Recomendação:** O sistema acumula as pontuações de risco de cada subsistema ao longo de todos os ciclos. A área que somar mais pontos é isolada pelo algoritmo, disparando um gatilho (`match/case`) com uma recomendação técnica específica de mitigação.

---

## 💻 Como Executar o Sistema

### Pré-requisitos
* Python 3.10 ou superior instalado (necessário suporte para a estrutura `match/case` utilizada no código).

### Execução
1. Faça o download ou clone o arquivo do script do projeto:
```bash
   git clone [https://github.com/equipe31ccpj/Mission-Control-AI.git](https://github.com/equipe31ccpj/Mission-Control-AI.git)
```

2. Navegue até o diretório e execute o arquivo principal via terminal:
```bash
   python main.py
```

## 👥 Integrantes
Nome: Akin Alexandre       RM: 572773
Nome: Maria Eduarda Rocha  RM: 570554
Nome: Pedro Henrique Neves RM: 571382