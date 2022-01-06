#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:14:59 2021

@author: lyliana
"""
import numpy as np


nU = 11223740
np.random.seed(nU)


def gera_w(nREP=1, Nx=1, Ny=1):
  x0 = 15
  y0 = 40
  sx = 2
  sy = 3
  w = np.zeros(nREP)
  for i in range(nREP):
    x = x0 + sx*np.random.randn(Nx)
    xm = np.mean( x )
    y = y0 + sy*np.random.randn(Ny)
    ym = np.mean( y )
    w[i] = xm * ym
  return w
print("a) Determine o valor médio, wm, e o desvio-padrão amostral, sm, dos valores de w.")
a = gera_w(10_000, Nx=1, Ny=1)
print("wm",np.mean(a))
print( "sw",np.std(a,ddof=1) )
print( "swm",(np.std(a,ddof=1)/np.sqrt(10_000) ))

print("b.1) Duas medições de x (Nx = 2) e apenas uma de y (Ny = 1)")
b1 = gera_w(10_000, Nx=2, Ny=1)
print( "sw",np.std(b1,ddof=1) )
print( "swm",(np.std(b1,ddof=1)/np.sqrt(10_000) ))

print("b.2) Duas medições de x (Nx = 1) e apenas uma de y (Ny = 2)")
b2 = gera_w(10_000, Nx=1, Ny=2)
print( "sw",np.std(b2,ddof=1) )
print( "swm",(np.std(b2,ddof=1)/np.sqrt(10_000) ))

print("c) Nx que minimiza a incerteza.")
for i in range(1,11,1):
    sw = np.std(gera_w(10_000, Nx=i, Ny=11-i),ddof=1) 
    swm = sw/np.sqrt(10_000)
    print(f'Nx = {i} e Ny = {11-i} -> swm = {swm:.2f} -> sw = {sw:.2f}')