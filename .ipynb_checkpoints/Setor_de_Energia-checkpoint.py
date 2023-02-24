#Analise de rendimentos de turbinas eolicas
#David Costa Pereira
#25/01/2023
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
#Lendo o arquivo
turbina = pd.read_csv('input/T1.csv')
turbina.columns = ['Date/Time', 'ActivePower(kW)', 'WindSpeed(m/s)', 'Curva_Teorica(KWh)', 'Wind Direction (°)']
del turbina['Wind Direction (°)']
turbina['Date/Time'] = pd.to_datetime(turbina['Date/Time'])
#Plotando o grafico - REAL
sns.scatterplot(data=turbina, x='WindSpeed(m/s)', y='ActivePower(kW)')
plt.show()
#Plotando o grafico - TEORICO
sns.scatterplot(data=turbina, x='WindSpeed(m/s)', y='Curva_Teorica(KWh)')
plt.show()
#Criando limites de desempenho
pot_real = turbina['ActivePower(kW)'].tolist()
pot_teorica = turbina['Curva_Teorica(KWh)'].tolist()
pot_max = []
pot_min = []
dentro_limite = []

for potencia in pot_teorica:
    pot_max.append(1.05*potencia)
    pot_min.append(0.95*potencia)
for p, potencia in enumerate(pot_real):
    if potencia>=pot_min[p] and potencia<=pot_max[p]:
        dentro_limite.append('Dentro')
    elif potencia == 0:
        dentro_limite.append('Zero')
    else:
        dentro_limite.append('Fora')
print(dentro_limite.count('Dentro')/len(dentro_limite))
#Adicionando dados ao nosso dataframe
turbina['DentroLimite'] = dentro_limite
#Grafico final
cores = {'Dentro':'blue','Fora':'red','Zero':'orange'}
sns.scatterplot(data=turbina, x='WindSpeed(m/s)', y='ActivePower(kW)', hue='DentroLimite', s=1, palette=cores)
plt.show()
