#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:26:33 2021

@author: lyliana

Gere N = 10.000 dados x com distribuição gaussiana de valor verdadeiro x0 = 50 e desvio-
padrão verdadeiro σ0 = 15. Em seguida, calcule:

1.1) O valor médio de x, xm, e sua incerteza;
1.2) O desvio-padrão amostral de x, σx;
1.3) O número de dados x no intervalo entre x0 − σ0 e x0 + σ0;
1.4) O número de dados x no intervalo entre x0 − 2σ0 e x0 + 2σ0;
1.5) O número de dados x no intervalo entre x0 − 3σ0 e x0 + 3σ0;
"""
import math
import numpy as np
import matplotlib.pyplot as plt
N = 10000
x0 = 50
s0 = 15
x = np.zeros(N)
Numero_1σ0 = 0
Numero_2σ0 = 0
Numero_3σ0 = 0
np.random.seed(11223740)

for i in range(N):
  x_conta = x0 + s0 * np.random.randn()
  x[i] = x_conta

h = plt.hist(x, bins=200, density=True)
xm = np.mean(x)
sx = np.std( x, ddof=1 )
sxm = sx/math.sqrt(N)
print( f' x_medio ~ {xm}' )
print( f'σ_xm ~ {sxm}' )
print( f'σx ~ {sx}' )

#Contando os pontos dentro dos intervalos
print((x0 - s0) <= x[99] <= (x0 + s0))

for i in range(N):
    if (x0 - s0) <= x[i] <= (x0 + s0):
        Numero_1σ0 += 1
for i in range(N):
    if (x0 - (2*s0))<= x[i] <= (x0 + (2*s0)):
        Numero_2σ0 += 1
for i in range(N):
    if (x0 - (3*s0)) <= x[i] <= (x0 + (3*s0)):
        Numero_3σ0 += 1

print( f'O número de dados x no intervalo entre x0 − 1σ0 e x0 + 1σ0 é {Numero_1σ0}' )
print( f'O número de dados x no intervalo entre x0 − 2σ0 e x0 + 2σ0 é {Numero_2σ0}' )
print( f'O número de dados x no intervalo entre x0 − 3σ0 e x0 + 3σ0 é {Numero_3σ0}' )

print("Valor máximo de x é", max(x))
print("Valor minimo de x é", min(x))

fig = plt.plot( 1+np.arange(N), x, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {N:.0f} simulações com x_medio ~ {xm} e sx~ {sx} ')