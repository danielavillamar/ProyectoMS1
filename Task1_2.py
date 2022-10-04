## PROYECTO 1
## Daniela Villamar 19086, Luis Pedro García 19344, Fernando Garavito
## El tiempo promedio de permanencia de un cliente en cola
#Referencias: https://github.com/CJP0/M-M-s-K_Queue_Simulation, http://smartdrill.com/MMS-queueing-model.html

#Imports
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math

#Ritmo de llegada de clientes por hora
lam = 50
#Velocidad de despachos por hora
lam2 = 30
x = []
Wy = []
simWy = []
#Probando con 2, hasta 7 cajas como combinaciones de variables
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(lam, lam2, i, 8, 10000)
	quSim.simRun()
	simWy.append(quSim.avgWaitTime)
print('Sim :x = ', x, ', y = ', simWy)
plt.plot(x, simWy, 'ro-', label='sim')
plt.title('Tiempo promedio de cliente en cola')
plt.xlabel('Cajas')
plt.ylabel('Espera(mins)')
tempX = x

#Plot
for x, y in zip(tempX, simWy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()