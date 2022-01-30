v = input().split()

A, B, C = v


A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

trian = (A*C)/2
circ = pi*C**2
trap = ((A+B)*C) / 2
quadr = B * B
retan = B * A

print("TRIANGULO: {:.3f}".format(trian))
print("CIRCULO: {:.3f}".format(circ))
print("TRAPEZIO: {:.3f}".format(trap))
print("QUADRADO: {:.3f}".format(quadr))
print("RETANGULO: {:.3f}".format(retan))