import matplotlib.pyplot as plt
import numpy as np

def P(x, n):
    '''
    Returns the nth Legendre polynomial
    evaluated at x.
    '''
    if n == 0:
        return 1 * np.ones_like(x)
    
    elif n == 1:
        return x
    
    else:
        P_n_minus_2 = 1
        P_n_minus_1 = x
        for i in range(2, n+1):
            P_n = ((2*i - 1) * x * P_n_minus_1 - (i - 1) * P_n_minus_2) / i
            
            P_n_minus_2 = P_n_minus_1
            P_n_minus_1 = P_n
            
        return P_n


# # Plot the first 6 Legendre polynomials over [-1, 1]
# x = np.linspace(-1, 1, 1000)
# fig, ax = plt.subplots()
# ax.axhline(0.0, color="#888888")

# # for n in range(6):
# for n in [8]:
#     Pn = P(x, n)
#     ax.plot(x, Pn, label=f'n = {n}')

# ax.set(xlabel=r'$x$', ylabel=r'$P_n(x)$')
# ax.legend()
# plt.show()


def bisection(F, a, b, tol):
    '''
    Returns the root of F in [a, b], found
    by bisection algorithm, within an error
    of tol.
    '''
    # Calculate the first midpoint
    c = (a + b) / 2
    
    # Loop until F(c) is close enough to zero
    while abs(F(c)) > tol:
        if F(a) * F(c) > 0:
            a = c
        else:
            b = c
        
        # Calculate the new midpoint
        c = (a + b) / 2
    
    return c


# Find all n roots
n = 8
tol = 1e-10
intervals = [[-1, -0.86],
             [-0.86, -0.68],
             [-0.68, -0.35],
             [-0.35, 0],
             [0, 0.35],
             [0.35, 0.68],
             [0.68, 0.86],
             [0.86, 1]]
             

def F(x):
    return P(x, n)

# Make a list to hold all roots
xk = []

# Compute each root
for intvl in intervals:
    xk.append(bisection(F, intvl[0], intvl[1], tol))


# Plot the nth Legendre polynomial over [-1, 1]
x = np.linspace(-1., 1., 1000)
fig, ax = plt.subplots()
ax.axhline(0.0, color="#888888")

ax.plot(x, F(x), label=f'n = {n}')
ax.plot(xk, F(np.array(xk)), 'ro', markersize=10, label='Bisection roots')

ax.set(xlabel=r'$x$', ylabel=r'$P_n(x)$')
ax.legend()
plt.show()
