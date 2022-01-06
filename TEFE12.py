#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:27:39 2021

@author: lyliana
"""
# Avaliação da tendenciosidade do desvio-padrão amostral
import numpy as np
import matplotlib.pyplot as plt

nU = 11223740
np.random.seed(nU)

x0 = 0
s0 = 1
M = 10_000
N = 3
hists = np.zeros(M)
histV = np.zeros(M)
Nvec = [100,50,10,5,4,3,2]
for N in Nvec:  
    print(f'\nCaso N = {N}\n')
    x = x0 + s0*np.random.randn(M,N)
    
    for i in range(M):
        hists[i] = np.std(x[i])
        histV[i] = ( hists[i])**2
    
    sx = np.std( x, axis=1, ddof=1 )
    sxm = np.mean(sx)
    s_sx = np.std( sx, ddof=1)
    s_sxm = s_sx/np.sqrt(len(sx))
    print( 'sxm = %.4f' % sxm )
    print( 'inc_sxm = %.4f ' % s_sxm )
    
    vx = sx**2
    vxm = np.mean(vx)
    s_vx = np.std(vx,ddof=1)
    s_vxm = s_vx/np.sqrt(len(vx))
    print( 'vxm = %.3f' % vxm )
    print( 'inc_vxm = %.3f ' % s_vxm )
       
    sumsx = sum(sx<s0)
    sumvx = sum(vx<(s0**2)) 
    print(sumsx)
    print(sumvx)
"""   
plt.hist(hists, bins='auto')
plt.title(f'Histograma de s para caso N = {N}')

textstr = '\n'.join((
    r's = %.4f' % (sxm, ),
    r'V = %.3f' % (vxm, ),
    r'N° s <= s0 = %.0f' % (sumsx, ),
    r'N° V <= V0 = %.0f' % (sumvx, )))

props = dict(boxstyle='round', alpha=0.5)
plt.text(0.05, 0.95, textstr,fontsize=14,horizontalalignment='right',verticalalignment='top',  bbox=props)

plt.show()
    
plt.hist(histV, bins='auto')
plt.title(f'Histograma de V para caso N = {N}')

textstr = '\n'.join((
    r's = %.4f' % (sxm, ),
    r'V = %.3f' % (vxm, ),
    r'N° s <= s0 = %.0f' % (sumsx, ),
    r'N° V <= V0 = %.0f' % (sumvx, )))

props = dict(boxstyle='round', alpha=0.5)
plt.text(0.05, 0.95, textstr,fontsize=14,horizontalalignment='right',verticalalignment='top',  bbox=props)

plt.show()"""