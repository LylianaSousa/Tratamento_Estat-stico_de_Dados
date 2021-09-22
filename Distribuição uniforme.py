#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:26:33 2021

@author: lyliana
Gere N = 10.000 dados y com distribuição uniforme no intervalo entre -10 e +10. Com base
nesses dados e sabendo que o valor verdadeiro de uma distribuição uniforme entre A e B é
y0 = (A+B)/2 e que o desvio-padrão verdadeiro é σ0 = (B−A)/√12, calcule:

2.1) O valor médio de y, ym, e sua incerteza;
2.2) O desvio-padrão amostral de y, σy;
2.3) O número de dados y no intervalo entre y0 − σ0 e y0 + σ0;
2.4) O número de dados y no intervalo entre y0 − 2σ0 e y0 + 2σ0;
2.5) O número de dados y no intervalo entre y0 − 3σ0 e y0 + 3σ0;
"""
import math
import numpy as np
import matplotlib.pyplot as plt
N = 10000
y0 = 0
s0 = 20/math.sqrt(12)
y = np.zeros(N)
Numero_1σ0 = 0
Numero_2σ0 = 0
Numero_3σ0 = 0
np.random.seed(11223740)

for i in range(N):
  y_conta = -10 + 20 * np.random.rand()
  y[i] = y_conta
  
h = plt.hist(y, bins=200, density=True)


ym = np.mean(y)
sy = np.std( y, ddof=1 )
sym = sy/math.sqrt(N)
print( f' y_medio ~ {ym}' )
print( f'σ_ym ~ {sym}' )
print( f'σy ~ {sy}' )

#Contando os pontos dentro dos intervalos
print((y0 - s0) <= y[99] <= (y0 + s0))

for i in range(N):
    if (y0 - s0) <= y[i] <= (y0 + s0):
        Numero_1σ0 += 1
for i in range(N):
    if (y0 - (2*s0))<= y[i] <= (y0 + (2*s0)):
        Numero_2σ0 += 1
for i in range(N):
    if (y0 - (3*s0)) <= y[i] <= (y0 + (3*s0)):
        Numero_3σ0 += 1

print( f'O número de dados y no intervalo entre y0 − 1σ0 e y0 + 1σ0 é {Numero_1σ0}' )
print( f'O número de dados y no intervalo entre y0 − 2σ0 e y0 + 2σ0 é {Numero_2σ0}' )
print( f'O número de dados y no intervalo entre y0 − 3σ0 e y0 + 3σ0 é {Numero_3σ0}' )

print("Valor máximo de y é", max(y))
print("Valor minimo de y é", min(y))

fig = plt.plot( 1+np.arange(N), y, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {N:.0f} simulações com y_medio ~ {ym} e sy~ {sy} ')