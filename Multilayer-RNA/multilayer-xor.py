#!/usr/bin/env python3

w1 = 1;
w2 = 1;
w3 = 1;
w4 = -1;
b1 = -0.5
b2 = -1.5
b3 = -0.5

def f(x1, x2, instancia):
  print("\n ------- INSTANCIA: " + str(instancia) + " -------")
  v1 = x1 * w1 + x2 * w2 + b1 #camada oculta
  v2 = x1 * w1 + x2 * w2 + b2 #camada oculta
  v3 = passo(v1) * w3 + passo(v2) * w4 + b3
  print("v1 = " + str(x1) + "*" + str(w1) + "+" + str(x2) + "*" + str(w2) + "+" + str(b1) + " = " + str(v1))
  print("v2 = " + str(x1) + "*" + str(w1) + "+" + str(x2) + "*" + str(w2) + "+" + str(b2) + " = " + str(v2))
  print("v3 = " + str(passo(v1)) + "*" + str(w3) + "+" + str(passo(v2)) + "*" + str(w4) + "+" + str(b3) + " = " + str(v3))
  y = passo(v3)
  return y

def passo(v):
  return 1 if v >= 0 else 0

def main():
  dataset = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
  ]
  for instancia in dataset:
    x1 = instancia[0]
    x2 = instancia[1]
    y = f(x1, x2, instancia)
    msg = "f(" + str(x1) + ", " + str(x2) + ") = " + str(y) + "\n"
    print(msg)

main()
