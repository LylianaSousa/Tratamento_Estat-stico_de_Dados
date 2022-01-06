#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 21:04:12 2021

@author: lyliana
"""
import numpy as np

np.random.seed(11223740)

N = 10000
n = 0
for i in range(N):
    x = np.random.rand()
    y = np.random.rand()
    if ( (x**2 + y**2)<=1 ):
        n = n+1

print("Questão 1 \n")
print( 'Valor de n obtido ~', n)
p = n/N
inc_n = np.sqrt(N*p*(1-p))
print( f'Incerteza no valor de n ~ {inc_n:.0f} \n' )

print("Questão 2 \n")
piMC = 4*(n/N)
print( 'PI experimental ou x ~', piMC)
inc_x = 4*(inc_n/N)
print( f'Incerteza no valor de n ~ {inc_n:.3f} \n')
print( f'Incerteza no valor de x ~ {inc_x:.3f} \n')

print("Questão 3 \n")
pved = np.pi/4
inc_nved = np.sqrt(N*pved*(1-pved))
inc_xved = 4*(inc_nved/N)
print( f'o desviopadrão verdadeiro de n ~ {inc_nved:.0f} \n' )
print( f'o desviopadrão verdadeiro de x ~ {inc_xved:.3f} \n' )

print("Questão 4 \n")
Nest = (16/(0.001*piMC)**2)*pved*(1-pved)
print( f'qual se aproxima mais do valor previsto para N ~ {Nest:.3f} \n' )
