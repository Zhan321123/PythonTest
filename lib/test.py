import math

h = 2
h0 = 1
T = 5
l = 20.942
D = 0.01 * 0.001
k = 2 * math.pi / l
am = h0 / 2 / math.sinh(k * h)
um = 2 * math.pi / T * am
delta = 2.5 * D
fw = math.exp(5.123 * (am / delta) ** -0.194 - 5.977)
rho = 1025
tau = rho * fw * um ** 2 / 2
print(um)
print(tau)

print(0.76*(math.tan(1/39.01)**(1/7)*(1/39.01)**(-1/4)*1))