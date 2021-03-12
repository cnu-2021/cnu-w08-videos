import numpy as np
import matplotlib.pyplot as plt

def F(x):
    return np.sin(2.0 * np.pi * x) * np.exp(4.0 * x) + x


def regula_falsi_error(F, a, b, tol):
    '''
    Finds the root of F in the interval [a, b] using
    the regula falsi method, to within an error of tol.
    '''
    # Iteration count
    its = 0
    
    # Initial x-intercept
    c = (a * F(b) - b * F(a)) / (F(b) - F(a))
    
    # Store all guesses
    x = [c]
    
    # Loop until the root is found
    while abs(F(c)) >= tol:
        # Increment the iteration count
        its += 1

        if F(a) * F(c) <= 0.0:    # F(a) and F(c) have different signs (or one or both is zero) ...
            b = c                 # ... a root is between a and c (or equals a or c)
        else:
            a = c                 # Else, a root is between c and b (or equals b)
            
        # Find the next x-intercept c
        c = (a * F(b) - b * F(a)) / (F(b) - F(a))
        x.append(c)
    
    # Return the root and the number of iterations
    return np.array(x), its


# Initial interval
a = 0.1
b = 0.7

# Tolerance
tol = 1e-10

# Run the algorithm, compute the error between all guesses
# and the final solution
x_rf, its = regula_falsi_error(F, a, b, tol)
e_rf = np.abs(x_rf[:-1] - x_rf[-1])

# Compute the ratios rk
rk = e_rf[1:] / e_rf[:-1]

# Compute and plot pk
pk = np.log(rk[1:]) / np.log(rk[:-1])
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(range(len(pk)), pk, 'b+')
ax.set(xlabel='Iteration', ylabel=r'$p_k$', title='Order of convergence for regula falsi')
#  plt.show()
