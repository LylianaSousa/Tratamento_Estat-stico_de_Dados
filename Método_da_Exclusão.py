#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:00:11 2021

@author: lyliana

Exemplo de rotina para gerar dados pelo Método da Exclusão
"""
import numpy as np # Biblioteca para manipulacao numerica


def metodo_exclusao(N):
    """
    Gera um vetor de N elementos
    """
    
    # PDF do exemplo do roteiro: f(x) = 2 * x com x entre 0 e 1
    xmin = 0
    xmax = 1
    ymax = 2
    f = lambda x : 2 * x
    
    i = 0
    x = np.zeros(N)
    while i < N:
        # gera um possivel x com distribuicao uniforme entre xmim e mxmax
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        # gera um valor de y para comparacao com a PDF no ponto x gerado
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1
    
    return x

N = 100
print(metodo_exclusao(N))