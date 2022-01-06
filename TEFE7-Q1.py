#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 21:35:23 2021

@author: lyliana
"""
# Lyliana Myllena Santos de Sousa
import numpy as np
import matplotlib.pyplot as plt


nU = 11223740
np.random.seed(nU)

N = 450
def gera_x(N=450):
  g = np.random.rand(N)
  x = np.power(125*g,1.0/3)
  return x

x = gera_x(N)
y = plt.hist( x, bins=range(0,6) )
plt.show()

def histograma_x(X):
  n = np.zeros(5)
  for x in X:
    if (x>=4):
      n[4] += 1
    elif (x>=3):
      n[3] += 1
    elif (x>=2):
      n[2] += 1
    elif (x>=1):
      n[1] += 1
    else:
      n[0] += 1
  return n

nh = histograma_x(x)
print( 'nh=', nh )
print( 'snh=', np.sqrt(nh*(1-nh/N)))
print()
print( 'De forma organizada:')
for i, n in enumerate(nh):
  print( f'[{i},{i+1}[ n={n:3.0f}  sn={np.sqrt(n*(1-n/N)):2.0f}' )

nREP = 10_000
n_01 = np.zeros(nREP)
n_12 = np.zeros(nREP)
n_23 = np.zeros(nREP)
n_34 = np.zeros(nREP)
n_45 = np.zeros(nREP)

for j in range(nREP):
  x = gera_x(N)
  nh_j = histograma_x(x)
  n_01[j] = nh_j[0]
  n_12[j] = nh_j[1]
  n_23[j] = nh_j[2]
  n_34[j] = nh_j[3]
  n_45[j] = nh_j[4]

print("\n")

nm01 = np.mean(n_01)
std_n01 = np.std( n_01, ddof=1 )
inc_nm01 = std_n01/np.sqrt(nREP)
print( 'n_01 médio = ', nm01 )
print( 'inc n_01 médio = ', inc_nm01 )
print( 'desv. pad. n01 = ', std_n01 )

print("\n")

nm12 = np.mean(n_12)
std_n12 = np.std( n_12, ddof=1 )
inc_nm12 = std_n12/np.sqrt(nREP)
print( 'n_12 médio = ', nm12 )
print( 'inc n_12 médio = ', inc_nm12 )
print( 'desv. pad. n12 = ', std_n12 )

print("\n")

nm23 = np.mean(n_23)
std_n23 = np.std( n_23, ddof=1 )
inc_nm23 = std_n23/np.sqrt(nREP)
print( 'n_23 médio = ', nm23 )
print( 'inc n_23 médio = ', inc_nm23 )
print( 'desv. pad. n23 = ', std_n23 )

print("\n")

nm34 = np.mean(n_34)
std_n34 = np.std( n_34, ddof=1 )
inc_nm34 = std_n34/np.sqrt(nREP)
print( 'n_34 médio = ', nm34 )
print( 'inc n_34 médio = ', inc_nm34 )
print( 'desv. pad. n34 = ', std_n34 )

print("\n")

nm45 = np.mean(n_45)
std_n45 = np.std( n_45, ddof=1 )
inc_nm45 = std_n45/np.sqrt(nREP)
print( 'n_45 médio = ', np.mean(n_45) )
print( 'inc n_45 médio = ', np.std( n_45, ddof=1)/np.sqrt(nREP) )
print( 'desv. pad. n45 = ', np.std( n_45, ddof=1) )

print("\n")

