#!/usr/bin/env python3
import numpy as np
import math
import sys
# exercício: implementar MLP xor usando um tensor de ordem superior
# obs: não usaremos tensores de ordem superior nos demais exercícios

class Xor:

  def __init__(self):
    self.x = np.array([
      int(sys.argv[1]),
      int(sys.argv[2]),
      int(sys.argv[3]),
      int(sys.argv[4])
    ])

    # rnas são implementadas como tensores ou como grafos de tensores
    # exemplo usando um tensor único:
    self.camadas = [
      [                                 # primeira camada
        np.array([[1., 1., 1., 1.]]), # pesos
        np.array([-0.5,-1.5,-2.5,-3.5])        # biases
      ],
      [                                 # segunda camada
        np.array([1., -1., 1., -1.]),            # pesos
        np.array([-0.5])              # biases
      ],
    ]

    # o exemplo usará a função passo, cuja a derivada é 0.
    # obs: redes multimacadas usam outras funções de ativação como sigmoide logística e relu
    self.passo = np.vectorize(lambda potencial: 1 if potencial >= 0 else 0)

  def ativaDataset(self):
    #print("nova ativação") # descomente para visão detalhada
    saida = self.ativaInstancia(0)
    #print("  f(" + str(instancia) + ") = " + str(saida))

  def ativaInstancia(self, i):
    sinal = self.x
    for c in range(len(self.camadas)):
      entrada = sinal
      pesos = self.camadas[c][0]
      biases = self.camadas[c][1]
      potencial = np.matmul(pesos, sinal) + biases
      sinal = self.passo(potencial)
      saida = sinal
      print(
        "i=" + str(i) +
        " c=" + str(c) +
        " x=" + str(entrada) +
        " w={:24s}".format(str(pesos.tolist())) +
        " b={:12s}".format(str(biases)) +
        " v=" + str(entrada) +
        " y=" + str(saida)
      )
      #print("  camada: " + str(c))
      #print("    entrada: " + str(sinal))
      #print("    potencial: " + str(potencial))
      #print("    saida: " + str(sinal))
    return sinal

  #def sigmoide(self, potencial):
  #  return 1 / (1 + math.exp(-potencial))

Xor().ativaDataset()

