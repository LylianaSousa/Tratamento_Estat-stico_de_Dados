"""
Considere uma grandeza P cuja relação com os dados U e R é dada por
P =U**2 /R. Suponha que U e R sejam gaussianos com valores verdadeiros
U0 = 16,0 V e R0 = 4,0 Ω e desvios-padrões (verdadeiros) σU = 0,5 V e
 σR = 0,5 Ω. 
"""
import numpy as np
N = 50000
U0 = 16.0
R0 = 4.0
sU = 0.5
sR = 0.5

P = np.zeros(N)
Prfixo = np.zeros(N)
Pufixo = np.zeros(N)

'''------------'''
print('Estime a incerteza de P')
for i in range(N):
  U = U0 + sU * np.random.randn()
  R = R0 + sU * np.random.randn()
  P[i] = (U**2)/R
Pm = np.mean(P)
sP = np.std( P, ddof=1 )

print( f' P_medio ~ {Pm}' )
print( f'inc. P ~ {sP}' )

import matplotlib.pyplot as plt
fig = plt.plot( 1+np.arange(N), P, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {N:.0f} simulações com P_medio ~ {Pm} e inc. P ~ {sP} ')

'''------------'''
print('simulações considerando o valor de R fixo')
for i in range(N):
  U = U0 + sU * np.random.randn()
  Prfixo[i] = (U**2)/R0
Prfixom = np.mean(Prfixo)
sPrfixo = np.std( Prfixo, ddof=1 )

print( f' Prfixo_medio ~ {Prfixom}' )
print( f'inc. Prfixo ~ {sPrfixo}' )

import matplotlib.pyplot as plt
fig = plt.plot( 1+np.arange(N), Prfixo, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {N:.0f} simulações com Prfixo_medio ~ {Prfixom} e inc. Prfixo ~ {sPrfixo} ')

'''------------'''
print('simulações fixando o valor de U')
for i in range(N):
  R = R0 + sR * np.random.randn()
  Pufixo[i] = (U0**2)/R
Pufixom = np.mean(Pufixo)
sPufixo = np.std( Pufixo, ddof=1 )

print( f' Pufixo_medio ~ {Pufixom}' )
print( f'inc. Pufixo ~ {sPufixo}' )

import matplotlib.pyplot as plt
fig = plt.plot( 1+np.arange(N), Pufixo, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {N:.0f} simulações com Pufixo_medio ~ {Pufixom} e inc. Pufixo ~ {sPufixo} ')
