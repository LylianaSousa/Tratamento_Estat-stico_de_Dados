#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:09:25 2021

@author: lyliana
"""
import numpy as np
import matplotlib.pyplot as plt

def meuMMQ( Y, G, si ):
  """"
    Y é o vetor de dados
    G é uma matriz com [g1, g2, ...]
    si é um número ou o vetor de incertezas
  """
  if ( np.size(Y)!=np.shape(G)[0] ):
    print( 'ajuste não pode ser realizado: número de linhas da matriz G deve ser igual ao número de dados')
    return
  if np.size(si)==1:
    si = si*np.ones_like(Y)
  N = np.size(Y)
  P = np.shape(G)[1]
  D = np.zeros([P,1])
  M = np.zeros([P,P])
  for i in range(N):
    for linha in range(P):
      D[linha] += Y[i]*G[i,linha]/(si[i]**2)
      for coluna in range(P):
        M[linha,coluna] += G[i,linha]*G[i,coluna]/(si[i]**2)
  
  VA = np.linalg.inv(M)
  A = np.dot( VA, D )
  sA = np.sqrt( np.diag(VA) )
  sA = sA.reshape(A.shape)
  F = np.zeros([N,1])
  for i in range(N):
    for j in range(P):
      F[i] += A[j]*G[i,j]
  return A, sA, VA, F


DADOS = np.loadtxt('./dados_osciloscópio.txt')
t = DADOS[:,0]
Y = DADOS[:,1]
Y = Y.reshape(-1,1)

plt.figure()
plt.plot( t, Y, ',')
plt.xlabel( 'tempo (s)' )
plt.ylabel( 'Tensão (V)')
plt.title('Sinal senoidal de frequência 2 Hz')
plt.show()


f = 2 #Hz
si = 0.06 #V
g1 = np.cos(2*np.pi*f*t)
g2 = np.sin(2*np.pi*f*t)
G = np.transpose([g1, g2])
A, sA, VA, F = meuMMQ(Y, G, si)

#a) Obtenha o valor dos parâmetros ajustados ã1 e ã2
print( 'ã1 = ( %.4f # %.4f ) [V]' % (A[0], sA[0]) )
print( 'ã2 = ( %.4f # %.4f ) [V]' % (A[1], sA[1]) )

#b) Determine a covariância e o coeficiente de correlação
print( 'cov = %.12f  [V]' % (VA[0,1]) )
print( 'rho = %.3f ' % (VA[0,1]/(sA[0]*sA[1])) )

#c) Calcule a amplitude, A = ( ã1^2 + ã2^2)^1/2
amplitude = np.sqrt( A[0]**2 + A[1]**2)
inca = (A[0]*sA[0])/amplitude
incb = (A[1]*sA[1])/amplitude
incc = (2*A[0]*A[1]*VA[0,1])/(amplitude**2)
incamplitude = np.sqrt(inca**2 + incb**2 + incc**2)

print( 'A = ( %.4f # %.4f ) [V]' % (amplitude, incamplitude) )

#d) Gráfico sobrepondo os dados e a função ajustada e dos resíduos do ajuste
plt.figure()
plt.subplot(3,1,(1,2))
plt.plot( t, Y, '.')
plt.plot( t, F, '-r')
plt.ylabel( 'Tensão (V)' )
plt.title('Sinal senoidal de frequência 2 Hz')
plt.subplot(4,1,4)
plt.plot( t, Y-F, ',')
plt.xlabel( 'tempo (s)' )
plt.ylabel( 'Resíduo (V)' )
plt.grid()
plt.show()

#e) Calcule o Chi^2 e o NGL

ccont = 0
for i in range(len(t)):
    ccont += ((Y[i] - ((A[0]*np.cos(2*np.pi*f*t[i])) + (A[1]*np.sin(2*np.pi*f*t[i]))))/(si))**2
print( 'chi^2 = %.1f ' % (ccont) )

NGL = len(DADOS) - 2
print("NGL = ", NGL)