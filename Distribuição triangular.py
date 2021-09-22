#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:26:35 2021

@author: lyliana

Gere N = 10.000 dados z com distribuição triangular no intervalo entre 0 e +40 (cada valor
de z pode ser gerado como a soma de dois valores com distribuição uniforme entre 0 e +20).
Com base nesses dados e sabendo que uma distribuição triangular entre C e D tem valor
verdadeiro z0 = (C+D)/2 e desvio-padrão verdadeiro σ0 = (D−C)/√24, calcule:

3.1) O valor médio de z, zm, e sua incerteza;
3.2) O desvio-padrão amostral de z, σz;
3.3) O número de dados z no intervalo entre z0 − σ0 e z0 + σ0;
3.4) O número de dados z no intervalo entre z0 − 2σ0 e z0 + 2σ0;
3.5) O número de dados z no intervalo entre z0 − 3σ0 e z0 + 3σ0;
"""
import math
import numpy as np
import matplotlib.pyplot as plt
N = 10000
z0 = 20
s0 = 40/(math.sqrt(24))
z = np.zeros(N)
Numero_1σ0 = 0
Numero_2σ0 = 0
Numero_3σ0 = 0
np.random.seed(11223740)

for i in range(N):
  z_1 =  20 * np.random.rand()
  z_2 =  20 * np.random.rand()
  #z_1 = np.random.uniform(0,20)
  #z_2 = np.random.uniform(0,20)
  z[i] = z_1 + z_2

h = plt.hist(z, bins=200, density=True)

zm = np.mean(z)
sz = np.std( z, ddof=1 )
szm = sz/math.sqrt(N)
print( f' z_medio ~ {zm}' )
print( f'σ_zm ~ {szm}' )
print( f'σz ~ {sz}' )

#Contando os pontos dentro dos intervalos
print((z0 - s0) <= z[99] <= (z0 + s0))

for i in range(N):
    if (z0 - s0) <= z[i] <= (z0 + s0):
        Numero_1σ0 += 1
for i in range(N):
    if (z0 - (2*s0))<= z[i] <= (z0 + (2*s0)):
        Numero_2σ0 += 1
for i in range(N):
    if (z0 - (3*s0)) <= z[i] <= (z0 + (8*s0)):
        Numero_3σ0 += 1

print( f'O número de dados z no intervalo entre z0 − 1σ0 e z0 + 1σ0 é {Numero_1σ0}' )
print( f'O número de dados z no intervalo entre z0 − 2σ0 e z0 + 2σ0 é {Numero_2σ0}' )
print( f'O número de dados z no intervalo entre z0 − 3σ0 e z0 + 3σ0 é {Numero_3σ0}' )

print("Valor máximo de z é", max(z))
print("Valor minimo de z é", min(z))
