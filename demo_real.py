# This is a function to illustrate a special function involving a parameter t, saying
# f(t) is the integral of |sin(x)+tcos(x)|^{2} in the interval [0,2*pi].

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the integrand function
def integrand(x, t):
    return np.abs(np.sin(x) + t * np.cos(x))**2

# Define the function f(t)
def f(t):
    result, _ = quad(integrand, 0, 2 * np.pi, args=(t,))
    return result

# Generate values for t in the interval (-1, 1)
t_values = np.linspace(-1, 1, 400)
f_values = [f(t) for t in t_values]

# Plot the function f(t)
plt.plot(t_values, f_values, label=r'$f(t) = \int_0^{2\pi} |\sin(x) + t\cos(x)|^2 \, dx$')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Plot of f(t) for t in (-1, 1)')
plt.legend()
plt.grid(True)
plt.show()