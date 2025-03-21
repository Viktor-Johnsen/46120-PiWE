"""Practice understanding of function handles.

Use scipy.optimize.fsolve to find the closest root of a function.
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc


def eval_quadratic(x, a, b, c):
    """Evaluate f(x) = a*x^2 + b*x + c."""
    y = a * x**2 + b * x + c
    return y # parabola


def plot_quadratic(a, b, c, xplot=np.linspace(-5, 5, 301)):
    """Plot a quadratic function."""
    fig, ax = plt.subplots(figsize=(6, 3))  # initialize figure
    yplot = eval_quadratic(xplot, a, b, c)  # define y-values to plot
    ax.plot(xplot, yplot)  # plot the quadratic function
    ax.plot(xplot, np.zeros_like(xplot), '--', c='0.3', zorder=0)  # plot a zero-line
    ax.set(xlim=xplot[[0, -1]], xlabel='x', ylabel='y')  # add labels
    ax.grid()  # add a grid
    fig.tight_layout()  # rescale axes in figure to look nice
    return fig, ax


if __name__ == '__main__':
    # define constants for parabola coefficients and initial guess
    A, B, C = 1, 1, -12 # ----------------------------------------> expected roots are x = {-4, 3}

    #A, B, C = -5, 0, -10 # If B = 0 and A, C > 0, OR:
                         #    B = 0 and A, C < 0, there will be no roots.
                         # If there are NO roots then the fsolve function returns the global extrema trying to reach 0.
                         # A, C > 0: by minimizing
                         # A, C < 0: by maximizing

    X0 = np.array([0,1]) # Initial guess MUST be a np.ndarray
    # X0 = np.array([0])

    # plot the parabola and initial guess as an x
    fig, ax = plot_quadratic(A, B, C)
    ax.scatter(x=X0, y=np.zeros(len(X0)), s=75, marker='x', c='k', label='Initial guess'+('es' if len(X0)>1 else '') )

    # Call fsolve using the necessary arguments and keyword arguments
    x_root = sc.optimize.fsolve(func=eval_quadratic, x0=X0, args=(A, B, C))

    # Add the found root(s) to the plot as a red circle with a see-through center
    ax.scatter(x=x_root, y=eval_quadratic(x_root, A, B, C), s=75, marker='o', color='r', facecolors='none', label='Root'+ ('s' if len(X0)>1 else '') ) 
    ax.legend()
    plt.show()
