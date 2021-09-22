#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:15:09 2021

@author: lyliana
"""
import numpy as np # Biblioteca para manipulacao numerica

np.random.seed(11223740)

def metodo_exclusao(N=1):    
    # PDF do exercicio 1 da Ativ. 05: f(x) = A*(1-x²) com x entre -1 e 1
    xmin = -1
    xmax = 1
    ymax = 3/4
    f = lambda x : (3/4)*(1 - x**2)
    i = 0
    x = np.zeros(N)
    while i < N:
        # gera um possivel x com distribuicao uniforme entre xmim e mxmax
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        # gera um valor de y para comparacao com a PDF no ponto x gerado
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1    
    return x
N=10000
x = metodo_exclusao(N)
import matplotlib.pyplot as plt
plt.hist(x,50)
sx = np.std(x, ddof=1)
print( f'sx = {sx:.4f}')

s0 = 0.4472
i = x0 =  Numero_1σ0 =  Numero_2σ0 =  Numero_3σ0 = 0

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
'''
fig = plt.plot( 1+np.arange(N), x, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title('Médias obtidas')'''