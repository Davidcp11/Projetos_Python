import matplotlib.pyplot as plt

# Dados para o gráfico
categorias = ['Positive', 'Neutral', 'Negative']
valores = [108+29+51+9, 158+129+128+20+64, 40+38+5]

# Criar o gráfico de barras
plt.bar(categorias, valores)

# Adicionar rótulos aos eixos
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Adicionar um título
plt.title('1 ITAU T23')

# Exibir o gráfico
plt.show()