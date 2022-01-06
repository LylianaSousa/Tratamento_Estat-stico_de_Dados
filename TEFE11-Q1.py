#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:23:22 2021

@author: lyliana
"""
import numpy as np
import matplotlib.pyplot as plt

nU = 11223740
np.random.seed(nU)

a0 = 30
b0 = 20
sa = sb = 2

N = 500
n = 0
rho = 0.95

A, B = np.zeros(N), np.zeros(N)

for i in range(N):
  r1 = np.random.randn()
  r2 = np.random.randn()
  A[i] = a0 + sa*r1
  B[i] = b0 + sb*( rho*r1 + np.sqrt(1-rho**2)*r2)
  erro_a = A[i] - a0
  erro_b = B[i] - b0
  if erro_a > 0 and erro_b > 0 :
      n += 1
      #print(n)
  elif erro_a < 0 and erro_b < 0 :
      n += 1
#a.0)
plt.plot( A, B,'.')
plt.xlabel('a')
plt.ylabel('b')
plt.plot( A[(A-a0)*(B-b0)>0], B[(A-a0)*(B-b0)>0], '.g')
plt.plot( A[(A-a0)*(B-b0)<0], B[(A-a0)*(B-b0)<0], '.r')
plt.plot( [a0, a0], [b0-3*sa, b0+3*sa], '-k' )
plt.plot( [a0-3*sa, a0+3*sa], [b0, b0], '-k' )
plt.title(f'a x b, para rho = {rho}')
plt.show()

#a.1)
print("a.1) Conte o número de vezes, n, em que os erros de a e b tem o mesmo sinal, estime a incerteza de n.")
print('n = ',n)
sn = np.sqrt(n*(1-(n/N)))
print(f'sn = {sn:.0f}')

#a.2)
print("a.2) Determine a frequência relativa com que os erros de a e b têm o mesmo sinal")
f = n/N
print(f'f = {f:.3f}')
sf = sn/N
print(f'sf = {sf:.3f}')

#a.3)
print("a.3) Calcule a covariância amostral, Vab, e a correspondente correlação amostral,R")
am = np.mean(A)
bm = np.mean(B)
vab = 0
for i in range(N):
    vab += (A[i] - am)*(B[i] - bm)
    
Vab = (1/(N-1))*vab

sa = np.std(A,ddof=1)
sb = np.std(B,ddof=1)
R = Vab/(sa*sb)

sVab = sa*sb*np.sqrt((1 + R**2)/(N - 1))
sR = (1 - R**2)/np.sqrt(n - 1)
print(f'Vab = {Vab:.2f}')
print(f'sVab = {sVab:.2f}')
print(f'R = {R:.3f}')
print(f'sR = {sR:.3f}')

#a.4)
print("a.4) Para cada um dos N pares de valores de a e b, calcule a soma correspondente, w = a + b e determine o desvio-padrão amostral")
W = np.zeros(N)
for i in range(N):
    W[i] = A[i] + B[i]
    
wm = np.mean(W)
sW = wm/np.sqrt(2*(N-1))
print(f'wm = {wm:.1f}')
print(f'sW = {sW:.1f}')

print("a.5) Repita o item anterior para o caso da diferença entre a e b, z = a − b.")
Z = np.zeros(N)
for i in range(N):
    Z[i] = A[i] - B[i]
    
zm = np.mean(Z)
sZ = zm/np.sqrt(2*(N-1))
print(f'zm = {zm:.2f}')
print(f'sZ = {sZ:.2f}')

