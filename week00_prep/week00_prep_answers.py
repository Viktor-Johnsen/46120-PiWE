
import numpy as np
import pandas as pd
import scipy as sci
import matplotlib.pyplot as plt

# 1. Write a simple function
def greet(name):
    print(f"Hello, {name}!")
    return

greet('world')

# 2. If/else statements
def goldilocks(bed_size):
    goldilocks_height = 135 # [cm]
    if bed_size < 140: # [cm]
        return print("Too small!")
    elif bed_size > 150: # [cm]
        return print("Too large!")
    else:
        return print("Just right. :)")

goldilocks(139)
goldilocks(140)
goldilocks(151)
goldilocks(150)

# 3. For loops
'''def square_list(l):
    l_ = np.array(l.copy())
    l_ = l_**2
    return l_'''
def square_list(l):
    l_ = l.copy()
    for idx in range(len(l)):
        l_[idx] = l[idx]**2
    return l_

print(square_list([1,2,3]))

# 4. While loops
def fibonacci_stop(max_val):
    fibonacci_sequence = []
    fibonacci_sequence.append(1)
    while fibonacci_sequence[-1] < max_val:
        fibonacci_sequence.append(sum(fibonacci_sequence[-2:]))
    return fibonacci_sequence[:-1]

print(fibonacci_stop(30))

#5. Logical operators

def clean_pitch(x,status):
    x_ = x.copy()
    for idx in range(len(x)):
        if status[idx] == 0:
            x_[idx] = x[idx]
        else:
            x_[idx] = -999
    return x_

x = [-1,2,6,95] # "raw" pitch anble at four time steps
status = [1,0,0,0] # status signal
print(clean_pitch(x,status))

