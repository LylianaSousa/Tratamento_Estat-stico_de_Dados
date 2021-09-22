#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 10:59:25 2021

@author: lyliana
Exemplo de rotina para gerar dados pelo Método da Inversão
"""
import numpy as np # Biblioteca para manipulacao numerica


def metodo_inversao(N):
    """
    Gera um vetor de N elementos
    """
    
    # PDF do exemplo do roteiro: f(x) = 2 * x com x entre 0 e 1
    #  para a qual, g(x)=x^2, cuja inversa eh x(g)=sqrt(g)
    inv_g = lambda g : np.sqrt(g)
    
    # gera N valores de g com distribuicao uniforme entre 0 e 1
    g = np.random.rand(N)
    # calcula os valores de x correspondentes
    x = inv_g(g)
    
    return x
N = 100
print(metodo_inversao(N))