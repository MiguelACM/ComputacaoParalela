#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:50:56 2018

@author: Miguel Monteiro

Se x² + y² <= 1 então caiu dentro do circulo


EXERCICIO 2: REAL TIME: 1m52.195s
"""

import sys
import random
from mpi4py import MPI

randomPoints = int(sys.argv[1]) # assume valor dado pelo argumento na linha de comandos
n = randomPoints // 4  # numero de iteracoes para cada thread
insidePoints = 0  # Pontos que cairam dentro do circulo
comm = MPI.COMM_WORLD
myrank = comm.Get_rank()

# cada thread faz n iteracoes
for i in range(n):
    #random.randon() da um valor "aleatorio" entre 0 e 1
    x2 = random.random()**2 # x²
    y2 = random.random()**2 # y²
    if x2 + y2 <= 1:
        insidePoints += 1
print("Na thread: ",myrank,"houve ",insidePoints,"pontos interiores atingidos", 
      "num total de ",n," pontos\n")    
    
if myrank == 0:
    for p in range(1, MPI.COMM_WORLD.Get_size()):
        insidePoints += comm.recv(source=p) #insidePoints e a soma de todos os pontos em cada thread

    pi = 4 * insidePoints / randomPoints
        
    print("\nIteracoes: ",randomPoints,"\nPontos interiores: ",insidePoints)
    print("\nPi = ",pi)
else:
    comm.send(insidePoints, dest=0)