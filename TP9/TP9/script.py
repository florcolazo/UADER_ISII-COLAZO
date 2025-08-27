import matplotlib.pyplot as plt
import numpy as np

# Fórmulas del ejercicio
def E(s):
    return 8 * s**0.95

def td(e):
    return 2.4 * e**0.33

# Gráfico 1 - Esfuerzo vs Tamaño
s = np.linspace(0, 10000, 100)
e = E(s)

plt.plot(s, e)
plt.title("Esfuerzo según el tamaño")
plt.xlabel("Tamaño del proyecto (S)")
plt.ylabel("Esfuerzo (E)")
plt.grid(True)
plt.show()

# Gráfico 2 - Tiempo vs Esfuerzo
e2 = np.linspace(1, 500, 100)
t = td(e2)

plt.plot(e2, t)
plt.title("Tiempo calendario según el esfuerzo")
