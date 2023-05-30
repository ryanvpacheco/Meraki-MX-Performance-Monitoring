import meraki
import matplotlib.pyplot as plt
import matplotlib.animation as animation

API_KEY = 'ChaveApiAQUI'
serial_1 = 'SerialAQUI'  # Serial do dispositivo Mx1
serial_2 = 'SerialAQUI'  # Serial do dispositivo Mx2

dashboard = meraki.DashboardAPI(API_KEY)

# Configurações do gráfico
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6))
linhas = []
cores = ['#5DBB63', '#386FA4']  # Cores  cada mx
labels = ['Mx1', 'Mx2']

for i in range(2):
    linha, = ax.plot([], [], color=cores[i], lw=2, linestyle='-', label=labels[i])
    linhas.append(linha)

linha_alta = ax.plot([], [], color='#F34235', lw=1, linestyle='--', dashes=(5, 5), label='Limite de Utilização Alta')[0]
marcacao_75 = ax.axhline(y=75, color='gray', lw=1, linestyle=':', label='75% de Utilização Alta')

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)  # Define o limite superior do eixo y como 100

ax.set_xlabel('Tempo')
ax.set_ylabel('Score de Desempenho')
ax.set_title('Monitoramento MX', fontsize=16, fontweight='bold', color='#5DBB63')
ax.legend(loc='upper right')

x_dados = []
y_dados = [[] for _ in range(2)]  # Lista de listas para armazenar os dados de cada equipamento

score_texts = []  # Lista para armazenar os textos dos scores individuais

def init():
    for score_text in score_texts:
        score_text.set_text('')
    return score_texts

def atualizar_grafico(frame):
    try:
        respostas = [dashboard.appliance.getDeviceAppliancePerformance(serial_arcos),
                     dashboard.appliance.getDeviceAppliancePerformance(serial_bh)]
        scores_desempenho = [resposta['perfScore'] for resposta in respostas]
        consumos = [f'{labels[i]}: {score_desempenho}%' for i, score_desempenho in enumerate(scores_desempenho)]

        # Atualiza os dados do gráfico
        x_dados.append(frame)
        for i, score_desempenho in enumerate(scores_desempenho):
            y_dados[i].append(score_desempenho)

        # Limita o número de pontos exibidos no gráfico para manter um histórico
        max_pontos = 100
        if len(x_dados) > max_pontos:
            x_dados.pop(0)
            for i in range(2):
                y_dados[i].pop(0)

        # Atualiza os dados das linhas do gráfico
        for i in range(2):
            linhas[i].set_data(x_dados, y_dados[i])
        
        linha_alta.set_data([x_dados[0], x_dados[-1]], [75, 75])  # Linha tracejada de 75% de utilização

        # Altera a cor das linhas com base no score de desempenho
        for i, score_desempenho in enumerate(scores_desempenho):
            if score_desempenho >= 75:
                linhas[i].set_color('#F34235')  # Vermelho para indicar alta utilização
                ax.set_facecolor('#FFECE9')  # Fundo vermelho claro
            else:
                linhas[i].set_color(cores[i])  # Cor do equipamento para indicar utilização normal
                ax.set_facecolor('#E9FCEB')  # Fundo verde claro

            # Atualiza o texto do score individual
            score_text = score_texts[i]
            score_text.set_text(consumos[i])
            if score_desempenho >= 75:
                score_text.set_color('#F34235')
            else:
                score_text.set_color('black')
        
        # Exibe o score atual de cada equipamento
        for i, score_desempenho in enumerate(scores_desempenho):
            score_text = score_texts[i]
            score_text.set_position((5, 95-i*5))
        
    except meraki.APIError as e:
        print(f"Ocorreu um erro na chamada da API: {e}")
    except Exception as ex:
        print(f"Ocorreu um erro desconhecido: {ex}")

# Cria os textos dos scores individuais
for i, _ in enumerate(labels):
    score_text = ax.text(5, 95-i*5, '', ha='left', va='top', fontsize=12, fontweight='bold', color='black', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))
    score_texts.append(score_text)

# Cria a animação
ani = animation.FuncAnimation(fig, atualizar_grafico, frames=range(1, 100), init_func=init, interval=1000)

# Exibe o gráfico
plt.tight_layout()
plt.show()
