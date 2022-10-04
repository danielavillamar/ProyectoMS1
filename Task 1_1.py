## PROYECTO 1
## Daniela Villamar 19086, Luis Pedro García 19344, Fernando Garavito
## Número promedio de clientes en el super/ sistema
#Referencias: https://github.com/CJP0/M-M-s-K_Queue_Simulation, http://smartdrill.com/MMS-queueing-model.html

#Imports
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math
    
#Ritmo de llegada de clientes por hora
lam = 50
#Velocidad de despachos por hora
lam2 = 40
x = []
simLy = []

#Probando con 2, hasta 7 cajas
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(lam, lam2, i, 8, 20000)
	quSim.simRun()
	simLy.append(quSim.avgWaitLen)
print('SIM :x = ', x, ', y = ', simLy)
plt.plot(x, simLy, 'ro-', label='sim')
plt.title('Numero de clientes promedio en cola dado "s" cajas')
plt.xlabel('s')
plt.ylabel('N')
tempX = x

#Plot
for x, y in zip(tempX, simLy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()