"""
Considere uma grandeza f cuja relação com os dados T e dada por f = 1/T. Suponha que
os dados T sejam gaussianos com valor verdadeiro T0 = 0,250 s e desvio-padrao
(verdadeiro) σT = 0,010 s. Estime a incerteza de f usando “Toy Monte Carlo” com N =
50.000 simulacos.
"""
import numpy as np
N = 50000
T0 = 0.250
sT = 0.010
f = np.zeros(N)
np.random.seed(11223740)

for i in range(N):
  T = T0 + sT * np.random.randn()
  f[i] = 1/T
fm = np.mean(f)
sf = np.std( f, ddof=1 )

print( f' f_medio ~ {fm}' )
print( f'inc.F ~ {sf}' )

import matplotlib.pyplot as plt
fig = plt.plot( 1+np.arange(N), f, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {N:.0f} simulações com f_medio ~ {fm} e inc. F ~ {sf} ')
