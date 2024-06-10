import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

def plot_function(f, a, b):
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
    plt.grid()
    plt.show()

def f(x):
    return x ** 2

a = 0
b = 2
plot_function(f, a, b)

def monte_carlo_integration(f, a, b, num_samples=10000):
    samples = [random.uniform(a, b) for _ in range(num_samples)]
    sample_values = [f(x) for x in samples]
    average_value = sum(sample_values) / num_samples
    integral_value = (b - a) * average_value
    return integral_value

integral_value = monte_carlo_integration(f, a, b)
print("Інтеграл методом Монте-Карло:", integral_value)

result, error = spi.quad(f, a, b)
print("Інтеграл функцією quad:", result)
