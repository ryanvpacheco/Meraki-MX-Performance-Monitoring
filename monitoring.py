import meraki
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Insira sua chave de API da Meraki aqui
API_KEY = 'API_AQUI'
# Insira o número de série do dispositivo MX aqui
serial = 'Serial_AQUI'

dashboard = meraki.DashboardAPI(API_KEY)

# Configurações do gráfico
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6))

# Linha principal do gráfico (score de desempenho)
linha, = ax.plot([], [], color='#5DBB63', lw=2, linestyle='-', label='Score de Desempenho')

# Linha tracejada representando o limite de utilização alta
linha_alta, = ax.plot([], [], color='#F34235', lw=1, linestyle='--', dashes=(5, 5), label='Limite de Utilização Alta')

# Linha horizontal representando 75% de utilização alta
marcacao_75 = ax.axhline(y=75, color='gray', lw=1, linestyle=':', label='75% de Utilização Alta')

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xlabel('Tempo')
ax.set_ylabel('Score de Desempenho')
ax.set_title('Monitoramento MX', fontsize=16, fontweight='bold', color='#5DBB63')
ax.legend(loc='upper right')

# Listas para armazenar os dados do gráfico
x_dados = []
y_dados = []

# Texto exibido no gráfico para o score atual
score_text = ax.text(0.05, 0.05, '', ha='left', va='bottom', transform=ax.transAxes, fontsize=14, fontweight='bold', color='black')

# Texto exibido no gráfico para a informação de utilização (alta ou normal)
utilizacao_text = ax.text(0.95, 0.05, '', ha='right', va='bottom', transform=ax.transAxes, fontsize=12)

def atualizar_grafico(frame):
    try:
        resposta = dashboard.appliance.getDeviceAppliancePerformance(serial)
        score_desempenho = resposta['perfScore']

        # Atualiza os dados do gráfico com o score de desempenho atual
        x_dados.append(frame)
        y_dados.append(score_desempenho)

        # Limita o número de pontos exibidos no gráfico para manter um histórico
        max_pontos = 100
        if len(x_dados) > max_pontos:
            x_dados.pop(0)
            y_dados.pop(0)

        # Atualiza as linhas do gráfico com os novos dados
        linha.set_data(x_dados, y_dados)
        linha_alta.set_data([x_dados[0], x_dados[-1]], [75, 75])  # Linha tracejada de 75% de utilização alta

        # Altera a cor da linha principal e do fundo com base no score de desempenho
        if score_desempenho >= 75:
            linha.set_color('#F34235')  # Vermelho para indicar alta utilização
            ax.set_facecolor('#FFECE9')  # Fundo vermelho claro
            utilizacao_text.set_text('Utilização Alta')
            utilizacao_text.set_color('#F34235')
        else:
            linha.set_color('#5DBB63')  # Verde para indicar utilização normal
            ax.set_facecolor('#E9FCEB')  # Fundo verde claro
            utilizacao_text.set_text('Utilização Normal')
            utilizacao_text.set_color('#5DBB63')

        # Atualiza o texto do score atual
        score_text.set_text(f'Score Atual: {score_desempenho}%')

    except meraki.APIError as e:
        print(f"Ocorreu um erro na chamada da API: {e}")

# Cria a animação
ani = animation.FuncAnimation(fig, atualizar_grafico, frames=range(1, 100), interval=1000)

# Exibe o gráfico
plt.tight_layout()
plt.show()
