
import scipy as sc

def fun(x):
    '''
    Algebraic function that maps an input x to an output y
    
    input:
        x : {float/int}
    output: 
        y : {float/int}
    '''
    y = 2*x - 4
    return y

def get_roots(fun, x0):
    '''
    Function that receives an algebraic function and a guess for the root and then return the root(s).
    
    input:
        fun: function {float/int} -> {float/int}
        x0 : {float/int}
    output:
        x_cross: {float/int}
        y_cross: {float/int}
    '''
    x_cross = sc.optimize.fsolve(func=fun, x0=x0)
    y_cross = fun(x_cross)
    return x_cross, y_cross

print(get_roots(fun=fun, x0=0))