#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:38:03 2021

@author: lyliana
"""
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

np.random.seed(11223740)


def gera_x_exclusao(N=1, xmin=-1, xmax=1, ymax= (3/2), f = lambda x: (3/2)*(x**2)):
  i = 0
  X = np.zeros(N)
  while (i<N):
    #gerar xcandidato
    xc = xmin + (xmax-xmin)*np.random.rand()
    #gerar y para verificacao
    yv = ymax * np.random.rand()
    if (yv <= f(xc) ):
      X[i] = xc
      i = i+1
  return X
M = 100
N = 10000
S = np.zeros(N)

x1 = gera_x_exclusao(N*M)
for i in range(N):
    Steste = 0
    for j in range(M):
       k = (N*(j-1)) + i
       Steste = Steste + x1[k]
       j = j + 1
    S[i] = Steste
sx = np.sqrt(3/5)
sS0 = sx*np.sqrt(M)
Snorm = S/sS0
plt.hist(Snorm,100)
plt.title(f'M = {M:.0f}')
print( f'M = {M:.0f}')
print( f'sS0 = {sS0:.2f}')
print( f'Assimetria = {st.skew(Snorm):.2f}')
print( f'Curtose excedente  = {st.kurtosis(Snorm):.2f}')

n1 = sum( np.abs(S)<=1*sS0 )
print( f'n(1) = {n1:.0f} (de um total de dados N={N:.0f})' )
n1_5 = sum( np.abs(S)<=1.5*sS0 )
print( f'n(1.5) = {n1_5:.0f} (de um total de dados N={N:.0f})' )
n2 = sum( np.abs(S)<=2*sS0 )
print( f'n(2) = {n2:.0f} (de um total de dados N={N:.0f})' )
n2_5 = sum( np.abs(S)<=2.5*sS0 )
print( f'n(2.5) = {n2_5:.0f} (de um total de dados N={N:.0f})' )
n3 = sum( np.abs(S)<=3*sS0 )
print( f'n(3) = {n3:.0f} (de um total de dados N={N:.0f})' )