import datetime as dt
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

'''----------------------------------------------------------------------'''
'''Derivada númerica'''


def Deriv_Ord1(xi, yi):
    n = len(xi)
    deriv = np.zeros(n)
    '''Para o primeiro ponto'''
    deriv[0] = (yi[1] - yi[0]) / (xi[1] - xi[2])
    '''Para os demais pontos'''
    for k in range(1, n - 1):
        deriv[k] = (yi[k + 1] - yi[k - 1]) / (xi[k + 1] - xi[k - 1])
    '''Para o último ponto'''
    deriv[n - 1] = (yi[n - 1] - yi[n - 2]) / (xi[n - 1] - xi[n - 2])
    return deriv


'''----------------------------------------------------------------------'''

'''Ler todos os arquivos da pasta'''
arquivos = os.listdir('Input_GPS')
'''Fazer o tratamento de dados para cada arquivo'''
for arquivo in arquivos:
    ler = open(f'Input_GPS/{arquivo}', 'r')
    for i in range(2):
        ler.readline()
    c = ler.readline()
    c = c.split()
    for i in range(2):
        ler.readline()
    coordenadas = [c[0], c[1], c[2]]
    n_stations = []
    Dados = [[[] for _ in range(3)] for _ in
             range(33)]  # numero do satelite(32 satelites), tempo e Vtec para cada satelite
    elev = int(15)  # int(input('Elevacao minima:'))
    for linha in ler:
        if linha:
            linha = linha.split()
            '''Tempo negativo = ausência de dados. Elevação mínima do satélite'''
            if float(linha[1]) >= 0 and float(linha[4]) >= elev and linha[1] and linha[8] and linha[5]:
                Dados[int(linha[2])][0].append(float(linha[1]))
                Dados[int(linha[2])][1].append(float(linha[8]))
                Dados[int(linha[2])][2].append(float(linha[5]))

    plt.figure(dpi=500)
    '''Latitudes máxima e mínima'''
    max_color = []
    min_color = []
    for i in range(1, 33):
        if Dados[i][2]:
            max_color.append(max(Dados[i][2]))
            min_color.append(min(Dados[i][2]))
    x1 = max(max_color)
    x2 = min(min_color)
    '''--------------------------------------'''
    '''Plotar 'Vtec vs tempo' para todos os satélites'''
    for i in range(1, 33):
        if Dados[i][2]:
            plt.scatter(Dados[i][0], Dados[i][1], s=0.1, marker=',', c=Dados[i][2], vmin=x2, vmax=x1, cmap='gist_ncar')
    plt.xlabel('UT (hrs)')
    plt.ylabel('TEC units')
    plt.colorbar(label='Latitude')
    Date = str(dt.datetime.today())
    plt.text(0, 54, f'Date:{Date[:10]} (Elev Mask {elev} deg)')
    plt.text(0, 56, f'Latitude(deg):{c[0]} Longitude(deg):{c[1]} Altitude(m):{c[2]}')
    plt.show()
    '''---------------------------------------------------------------------------'''
    '''Plotar o ROTi (para cada satélite)'''
    for i in range(1, 33):
        x = np.array(Dados[i][0])
        y = np.array(Dados[i][1])
        if len(x) == len(y) and len(x) > 0:
            rot = Deriv_Ord1(x, y)
            plt.plot(x, rot)
    plt.show()
