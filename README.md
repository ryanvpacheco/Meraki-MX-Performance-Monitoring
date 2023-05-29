Monitoramento de Desempenho do Dispositivo Meraki MX
Descrição

Este código cria um gráfico de monitoramento do desempenho de um dispositivo Meraki MX. O gráfico exibe o score de desempenho atual e o compara com um limite de utilização alta (75%). O fundo do gráfico e a cor da linha principal são atualizados com base no score de desempenho, indicando se a utilização está alta ou normal.
Pré-requisitos

    Python 3.x
    Bibliotecas: meraki, matplotlib

Como usar

    Substitua 'API_AQUI' pela sua chave de API da Meraki.
    Substitua 'Serial_AQUI' pelo número de série do dispositivo MX que deseja monitorar.
    Execute o código.

Resultado

Um gráfico será exibido, mostrando a evolução do score de desempenho ao longo do tempo. O texto indicará se a utilização está alta ou normal, e o score atual será exibido no canto superior esquerdo do gráfico.
Observações

    Certifique-se de ter as bibliotecas meraki e matplotlib instaladas antes de executar o código. Você pode instalá-las usando o pip: pip install meraki matplotlib.
    É necessário ter uma chave de API válida da Meraki para acessar os dados do dispositivo MX.
    Verifique se o número de série do dispositivo MX está correto.
    O gráfico será atualizado a cada segundo com um novo score de desempenho.
    
    
    
    
    _____________________________________________________________________________________________________________________________________
    # Meraki MX Device Performance Monitoring
## Description

This code creates a performance monitoring graph for a Meraki MX device. The graph displays the current performance score and compares it to a high utilization threshold (75%). The graph's background color and the color of the main line are updated based on the performance score, indicating whether the utilization is high or normal.

## Prerequisites

- Python 3.x
- Libraries: meraki, matplotlib

## How to Use

1. Replace `'API_AQUI'` with your Meraki API key.
2. Replace `'Serial_AQUI'` with the serial number of the MX device you want to monitor.
3. Run the code.

## Result

A graph will be displayed, showing the performance score's evolution over time. The text will indicate whether the utilization is high or normal, and the current score will be shown in the top-left corner of the graph.

## Notes

- Make sure you have the `meraki` and `matplotlib` libraries installed before running the code. You can install them using pip: `pip install meraki matplotlib`.
- A valid Meraki API key is required to access the MX device data.
- Verify that the MX device's serial number is correct.
- The graph will be updated every second with a new performance score.
