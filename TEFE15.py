#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:34:44 2021

@author: lyliana
"""
import numpy as np
import matplotlib.pyplot as plt

NUSP = 11223740
np.random.seed( NUSP )
def geraDados( N, x0=50, s0=10 ):
  x = np.zeros(N)
  for i in range(N):
    x[i] = x0 + s0*np.random.randn(1)
  sx = np.std( x, ddof=1 )
  xm = np.mean(x)
  sxm = sx/np.sqrt(N)
  return xm, sxm

x0 = 50
s0 = 10

#a) Considere N = 4
N = 4; t2 = 3.31
#N = 101; t2 = 2.03
print("z_2 = ", t2/np.sqrt(N))

#b) Para gerar N_REP = 10_000 conjuntos de N - teste t
nREP=10_000
tXMs = np.zeros(nREP)
tsXMs = np.zeros(nREP)
for i in range(nREP):
  tXMs[i], tsXMs[i] = geraDados( N )

tb = (tXMs-x0)/tsXMs
Vfb = sum(np.abs(tb)<=t2)
fb = Vfb/nREP
incfb = np.std(tb, ddof=1)/np.sqrt(len(tb))
print( 'f_t2 = ( %.4f # %.4f )' % (fb, incfb))

#c) Para gerar N_REP = 10_000 conjuntos de N - teste z
zXMs = np.zeros(nREP)
zsXMs = np.zeros(nREP)
for i in range(nREP):
  zXMs[i], zsXMs[i] = geraDados( N )

zc = (zXMs-x0)/(s0/np.sqrt(N))
Vfc = sum(np.abs(zc)<=2)
fc = Vfc/nREP
incfc = np.std(zc, ddof=1)/np.sqrt(len(zc))
print( 'f_z2 = ( %.4f # %.4f )' % (fc, incfc))




