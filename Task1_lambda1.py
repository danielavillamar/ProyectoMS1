## PROYECTO 1
## Daniela Villamar 19086, Luis Pedro García 19344, Fernando Garavito
## El tiempo promedio de permanencia de un cliente en cola
#Referencias: https://github.com/CJP0/M-M-s-K_Queue_Simulation, http://smartdrill.com/MMS-queueing-model.html

from MMSK.simulation import *
import matplotlib.pyplot as plt
import math

#Velocidad de despachos por hora
lam2 = 6
#Cajas
cajas = 2
x = []

simWqy = []
#Probando con velocidades de llegada desde 2 a 7
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(i, lam2, cajas, 8, 10000)
	quSim.simRun()
	simWqy.append(quSim.avgWaitQuTime)
	

print('SIM :x = ', x, ', y = ', simWqy)
plt.plot(x, simWqy, 'ro-', label='sim')

plt.title('Tiempo de espera con diferentes ritmos de llegada')
plt.xlabel('lambda1')
plt.ylabel('Espera en minutos')
tempX = x


for x, y in zip(tempX, simWqy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()