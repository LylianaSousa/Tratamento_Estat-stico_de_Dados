"""
Considere uma grandeza V cuja relação com os dados d é dada por V=(π/6)*d³.
Suponha que os dados d sejam gaussianos com valor verdadeiro d0=10,0 mm e 
desvio-padrão (verdadeiro) σd=2,0 mm.
"""
import numpy as np
N = 50000
d0 = 10.0
sd = 2.0
Pi = np.pi
V = np.zeros(N)
d = np.zeros(N)
for i in range(N):
  d = d0 + sd * np.random.randn()
  V[i] = ((Pi/6)*(d**3))
Vm = np.mean(V)
sV = np.std( V, ddof=1 )

print( f' v_medio ~ {Vm}' )
print( f'inc. v ~ {sV}' )

import matplotlib.pyplot as plt
fig = plt.plot( 1+np.arange(N), V, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {N:.0f} simulações com V_medio ~ {Vm} e inc. V ~ {sV} ')
