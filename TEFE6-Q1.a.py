#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:15:17 2021

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
N=10000
x = gera_x_exclusao(N)
plt.hist(x,50)
sx = np.sqrt(3/5)
print( f'sx = {sx:.2f}')
print( f'Assimetria = {st.skew(x):.2f}')
print( f'Curtose excedente  = {st.kurtosis(x):.2f}')

n1 = sum( np.abs(x)<=1*sx )
print( f'n(1) = {n1:.0f} (de um total de dados N={N:.0f})' )
n1_5 = sum( np.abs(x)<=1.5*sx )
print( f'n(1.5) = {n1_5:.0f} (de um total de dados N={N:.0f})' )
n2 = sum( np.abs(x)<=2*sx )
print( f'n(2) = {n2:.0f} (de um total de dados N={N:.0f})' )
n2_5 = sum( np.abs(x)<=2.5*sx )
print( f'n(2.5) = {n2_5:.0f} (de um total de dados N={N:.0f})' )
n3 = sum( np.abs(x)<=3*sx )
print( f'n(3) = {n3:.0f} (de um total de dados N={N:.0f})' )