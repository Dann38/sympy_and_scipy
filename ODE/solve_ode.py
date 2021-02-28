from sympy import *
import numpy as np
import matplotlib.pyplot as plt

init_printing(use_unicode=True)

x = symbols('x')
y = Function('y')

eq1 = Eq(y(x).diff(x), x**3)

res = dsolve(eq1, y(x), '1st_linear')
f = res.rhs

c1 = f.args[0]
C1 = range(-30, 50, 5)
t = np.linspace(-5, 5, 100)

for k in C1:
    f_ = f.subs({c1:k})
    ft = [f_.subs({x: i}) for i in t]

    plt.plot(t, ft)

plt.show()
