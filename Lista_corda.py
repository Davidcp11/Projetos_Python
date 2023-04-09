import matplotlib.pyplot as plt
# O pacote numpy permite criar arrays. Necessário para códigos numéricos mais eficientes em Python
import numpy as np
# importa a função para o cálculo da probabilidade chi2 contida no pacote estatístico stats
from scipy import stats
from sklearn.linear_model import LinearRegression
from scipy.stats import chi2
# Coloque seus dados, em txt, na forma: Massa, f1, f2, f3, f4
arq = open('dados_corda.txt', 'r')
dados_t = []
dados_y = []
for linha in arq:
    linha = linha.split(",")
    massa = float(linha[0])
    phi = np.sqrt(massa)
    # Dados t=nsqrt(M) (parametro ) e f (frequencia)
    dados_t.append(1*phi)
    dados_t.append(2*phi)
    dados_t.append(3*phi)
    dados_t.append(4*phi)
    dados_y.append(float(linha[1]))
    dados_y.append(float(linha[2]))
    dados_y.append(float(linha[3]))
    dados_y.append(float(linha[4]))

t = np.array(dados_t)
y = np.array(dados_y)
incertezas_x = np.array([0.005]*len(dados_t))
# Ajuste o modelo usando o scikit-learn
# Intercept false=passa pela origem
# Intercept true=nao necessariamente
model = LinearRegression(fit_intercept=False)
model.fit(t.reshape(-1, 1), y, sample_weight=1)
# Obtenha o coeficiente angular e sua incerteza
coef_angular = model.coef_[0]
dp_coef_angular = np.sqrt(np.sum((y - coef_angular * t)**2) / ((len(t) - 1) * np.sum(incertezas_x**2 * t**2)))
# Calcule as incertezas dos pontos y
incertezas_y = np.sqrt((dp_coef_angular * t)**2 + (incertezas_x * coef_angular)**2)
print(f"incerteza instrumental de L (cm) = 0.05")
print(f"coeficiente angular (Hz/g^0.5) = {coef_angular}")
# Calcule os valores previstos pelo modelo
y_pred = model.predict(t.reshape(-1, 1))
# Calcule os resíduos
residuos = y - y_pred
# Calcule o número de graus de liberdade
S = np.matmul(residuos.T, residuos)
ngl = len(y) - 1
sig_posteriori = np.sqrt(S/ngl)
variancia_coef_angular = 1 / ((sig_posteriori**2) * np.sum((t ** 2)))
sig_coef_ang = np.sqrt(variancia_coef_angular)
print(f"incerteza do coeficiente angular (Hz/g^0.5) = {sig_coef_ang}")
print(f"incerteza de f (Hz)(sigma_f) = {sig_posteriori})")
mu = 9.786 * (10 ** 5) / (4*(coef_angular**2) * 128**2)
print(f"valor de mu (mg/cm) = {mu}")
incerteza = 2 * mu * np.sqrt((0.05 / 128.0)**2 + (sig_coef_ang / coef_angular)**2)
print(f"incerteza de mu (mg/cm) = {incerteza}")

