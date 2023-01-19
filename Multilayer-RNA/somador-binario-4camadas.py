#!/usr/bin/env python3
# exercício: implementar testador de paridade impar (n=4)
import numpy as np
import sys

class ParidadeImpar:

  def __init__(self):
    passo = lambda potencial: 1 if potencial >= 0 else 0

    x1 = int(sys.argv[1])
    x2 = int(sys.argv[2])
    x3 = int(sys.argv[3])
    x4 = int(sys.argv[4])
    
    v1 = x2+x4-1.5
    y1 = passo(v1)
    v2 = x1+x3+y1-1.5
    y2 = passo(v2)
    v3 = y2-0.5
    y3 = passo(v3)
    v4 = x1-(2*y2)+x3+y1-0.5
    y4 = passo(v4)
    v5 = x2-(2*y1)+x4-0.5
    y5 = passo(v5)

    print(
      " y3=", y3,
      " y4=", y4,
      " y5=", y5, sep=""
    )

ParidadeImpar()
