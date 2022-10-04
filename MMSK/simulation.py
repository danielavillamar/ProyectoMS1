## PROYECTO 1
## Daniela Villamar 19086, Luis Pedro García 19344, Fernando Garavito
#Referencias: https://github.com/CJP0/M-M-s-K_Queue_Simulation, http://smartdrill.com/MMS-queueing-model.html


import numpy as np
import random
import math 
import queue

#Clase de cliente del super, cada uno con tiempos de llegada.
class customer:
	departTime = 0
	def __init__(self, at, st, s):
		self.arrivalTime = at
		self.serviceTime = st
		self.event = s

#Eventos (llegadas y salidas)
class simEventList:
	def __init__(self, lam, mu, n = 0):
		#Distribucion exponencial
		tempServiceTime = int(np.random.exponential(1/mu)*60)
		self.list = [customer(0, tempServiceTime, 'arrival')]
		#Cantidad de clientes y llegada Poisson
		for i in range(n-1):
			tempServiceTime = int(np.random.exponential(1/mu)*60)
			tempInterArrivalTime = int(np.random.exponential(1/lam)*60)
			self.list.append(customer(self.list[i].arrivalTime+tempInterArrivalTime, tempServiceTime, 'arrival'))
	
	
	def insertC(self, temp):
		i = 0
		for i in range(len(self.list)+1):
			if len(self.list) == i:
				break
			if self.list[i].arrivalTime > temp.arrivalTime:
				break
		
		self.list.insert(i, temp)
	
 
 #La cola, definiendo las variables como cantidad de servers, etc.
class queueSim:
	def __init__(self, lam, mu, s, k, n):
		self.lam = lam
		self.mu = mu
		self.s = s
		self.k = k
		self.availableServer = s
		self.customerNum = n
		self.waitQueue = queue.Queue(k-s)
		self.eventList = simEventList(lam, mu, n)
		self.currentTime = 0
		self.waitTimeAcc = 0
		self.waitQuTimeAcc = 0
		self.waitLenAcc = 0
		self.waitQuLenAcc = 0
		self.completedNum = 0
		self.servingNum = 0
		self.previousTime = 0
		
		#Correr la sim
	def simRun(self):
		while(self.eventList.list):
			temp = self.eventList.list.pop(0)
			self.waitLenAcc += ((self.currentTime - self.previousTime) * (self.servingNum + self.waitQueue.qsize()))
			self.waitQuLenAcc += ((self.currentTime - self.previousTime) * self.waitQueue.qsize())
			self.previousTime = self.currentTime
			self.currentTime = temp.arrivalTime
			if temp.event == 'depart':
				if not self.waitQueue.empty():
					temp2 = self.waitQueue.get()
					self.waitQuTimeAcc += self.currentTime - temp2.arrivalTime
					self.waitTimeAcc += (self.currentTime - temp2.arrivalTime) + temp2.serviceTime
					temp2.arrivalTime = self.currentTime + temp2.serviceTime
					temp2.event = 'depart'
					self.eventList.insertC(temp2)
				else:
					self.servingNum -= 1
					self.availableServer += 1
				self.completedNum += 1
			elif temp.event == 'arrival':
					#Si sí hay cajas disponibles
				if self.availableServer > 0:
					temp.arrivalTime += temp.serviceTime
					temp.event = 'depart'
					self.eventList.insertC(temp)
					self.waitTimeAcc += temp.serviceTime
					self.servingNum += 1
					self.availableServer -= 1
					#Si no hay cajas disponibles
				else:
					if not self.waitQueue.full():
						self.waitQueue.put(temp)
			
		self.avgWaitTime = self.waitTimeAcc/self.completedNum
		self.avgWaitQuTime = self.waitQuTimeAcc/self.completedNum
		self.avgWaitLen = (self.waitLenAcc/self.currentTime)
		self.avgWaitQuLen = (self.waitQuLenAcc/self.currentTime)

	
			
		self.avgWaitTime = self.waitTimeAcc/self.completedNum
		self.avgWaitQuTime = self.waitQuTimeAcc/self.completedNum
		self.avgWaitLen = (self.waitLenAcc/self.currentTime)
		self.avgWaitQuLen = (self.waitQuLenAcc/self.currentTime)
	
  
		