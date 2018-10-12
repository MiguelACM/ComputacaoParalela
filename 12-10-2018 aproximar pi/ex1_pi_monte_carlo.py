#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:50:56 2018

@author: Miguel Monteiro

Se x² + y² <= 1 então caiu dentro do circulo
"""

import sys
import random

randomPoints = int(sys.argv[1]) # n assume valor dado pelo argumento na linha de comandos
insidePoints = 0  # Pontos que cairam dentro do circulo

for i in range(randomPoints):
    #random.randon() da um valor "aleatorio" entre 0 e 1
    x2 = random.random()**2 # x²
    y2 = random.random()**2 # y²
    if x2 + y2 <= 1:
        insidePoints += 1
        
pi = 4 * insidePoints / randomPoints

print("\nIteracoes: ",randomPoints,"\nPontos interiores: ",insidePoints)
print("\nPi = ",pi)