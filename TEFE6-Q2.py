#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:23:27 2021

@author: lyliana
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

np.random.seed(11223740)


def gera_x_exponencial(N=1,L=1):
  g = np.random.rand(N)
  X = -L*np.log(1-g)
  return X
L=1
M = 1000
N = 10000
S = np.zeros(N)

x1 = gera_x_exponencial(N*M,L)
for i in range(N):
    Steste = 0
    for j in range(M):
       k = (N*(j-1)) + i
       Steste = Steste + x1[k]
       j = j + 1
    S[i] = Steste
sx = 1
sS0 = sx*np.sqrt(M)
x0 = 1
s0 = M*x0
Snorm = (S- s0)/sS0
plt.hist(Snorm,100)
plt.title(f'M = {M:.0f}')
print( f'M = {M:.0f}')
print( f'sS0 = {sS0:.2f}')
print( f'Assimetria = {st.skew(Snorm):.2f}')
print( f'Curtose excedente  = {st.kurtosis(Snorm):.2f}')

n1 = sum( np.abs(S- s0)<=1*sS0 )
print( f'n(1) = {n1:.0f} (de um total de dados N={N:.0f})' )
n1_5 = sum( np.abs(S- s0)<=1.5*sS0 )
print( f'n(1.5) = {n1_5:.0f} (de um total de dados N={N:.0f})' )
n2 = sum( np.abs(S- s0)<=2*sS0 )
print( f'n(2) = {n2:.0f} (de um total de dados N={N:.0f})' )
n2_5 = sum( np.abs(S- s0)<=2.5*sS0 )
print( f'n(2.5) = {n2_5:.0f} (de um total de dados N={N:.0f})' )
n3 = sum( np.abs(S- s0)<=3*sS0 )
print( f'n(3) = {n3:.0f} (de um total de dados N={N:.0f})' )