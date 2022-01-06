#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 09:05:41 2021

@author: lyliana
"""
import numpy as np
import matplotlib.pyplot as plt

nU = 11223740
np.random.seed(nU)

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

def meuPolinomio( grau, Y, x, si):
    
      G = np.zeros( [len(Y),grau+1] )
      
      for j in range(grau+1):
            for i in range(len(Y)):
                G[i,j] = x[i]**j
                
      return meuMMQ(Y, G, si)

#Dados artificiais para ajuste
t = [1, 2, 3, 4, 5]
g1 = np.ones(len(t))
g2 = np.array(t)
G = np.array([g1,g2]).T
Y = np.array([1.7, 3.0, 4.2, 4.8, 5.4])
si = 0.2
A, sA, VA, F = meuMMQ( Y, G, si )

print("\n Item a\n")

print( 'atil = ( %.2f # %.2f ) cm' % (A[0], sA[0]) )
print( 'btil = ( %.3f # %.3f ) cm/s' % (A[1], sA[1]) )
print( 'Matrix cov = ',  VA )
plt.figure
plt.title('Ajuste MMQ')
plt.errorbar( t, Y, si, fmt='*')
plt.plot( t, F, '-r' )
plt.show()
print("\n Item b\n")

print( 'cov = %.4f ' % (VA[0,1]) )
print( 'rho = %.3f ' % (VA[0,1]/(sA[0]*sA[1])) )

print("\n Item c\n")

ccont = 0
for i in range(len(t)):
    ccont += ((Y[i] - (A[0] + (A[1]*t[i])))/(si))**2
print( 'chi^2 = %.1f ' % (ccont) )

#O número de graus de liberdade é dado por:
#NGL = #dados - #parâmetros estimados 
NGL = len(t) - 2
print('NGL = ', NGL)

print("\n Item d\n")

def fajuste(t):
    valor = A[0] + (A[1]*t)
    incerteza = np.sqrt((sA[0])**2 + (sA[1]*t)**2)
    return valor, incerteza

valor1,incerteza1 = fajuste(1.5)
print( ' Posição da bolha em t = 1.5 s = ( %.2f # %.2f ) cm' % (valor1,incerteza1))

valor2,incerteza2 = fajuste(6)
print( ' Posição da bolha em t = 6 s = ( %.2f # %.2f ) cm' % (valor2,incerteza2))

print("\n Item e\n")
X = np.zeros(5)
for i in range(5):
    X[i] = t[i] - 3
ng1 = np.ones(len(X))
ng2 = np.array(X)
nG = np.array([ng1,ng2]).T
nY = np.array([1.7, 3.0, 4.2, 4.8, 5.4])
nsi = 0.2
nA, nsA, nVA, nF = meuMMQ( nY, nG, nsi )
print( 'alpha = ( %.2f # %.2f ) cm' % (nA[0], nsA[0]) )
print( 'beta = ( %.3f # %.3f ) cm/s' % (nA[1], nsA[1]) )
print( 'cov = ',(nVA[0,1]) )
print( 'rho = %.3f ' % (nVA[0,1]/(nsA[0]*nsA[1])) )
plt.figure
plt.title('Ajuste MMQ (translação)')
plt.errorbar( X, nY, nsi, fmt='*')
plt.plot( X, nF, '-r' )
plt.show()
nccont = 0
for i in range(len(X)):
    nccont += ((nY[i] - (nA[0] + (nA[1]*X[i])))/(nsi))**2
print( 'chi^2 = %.1f ' % (nccont) )

def nfajuste(X):
    valor = nA[0] + (nA[1]*X)
    incerteza = np.sqrt((nsA[0])**2 + (nsA[1]*X)**2)
    return valor, incerteza

nvalor1,nincerteza1 = nfajuste(-1.5)
print( ' Posição da bolha em X = -1.5 s = ( %.2f # %.2f ) cm' % (nvalor1,nincerteza1))

nvalor2,nincerteza2 = nfajuste(3)
print( ' Posição da bolha em X = 3 s = ( %.2f # %.2f ) cm' % (nvalor2,nincerteza2))
