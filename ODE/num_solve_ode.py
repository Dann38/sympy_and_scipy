from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def f(y, x):
    return x**3+np.exp(x)

y0_array = range(-3, 3, 1)
x = np.linspace(-2, 2, 100)

for y0 in y0_array:
    y = odeint(f, y0, x)
    plt.plot(x, y)
plt.show()
