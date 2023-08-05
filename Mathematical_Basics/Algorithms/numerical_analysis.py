# -*- coding: utf-8 -*-
"""
Numerical Analysis Algorthims
"""
import numpy as np
import pandas as pd

# Bisection Method Algorithm
def bisection_approx(root, points, iters = 5):
    a, b = points
    bisection_tracker = pd.DataFrame(columns = ['a', 'b', 't', 'f(a)', 'f(b)', 'f(t)'])
    for iteration in range(iters):
        # endpoint calcs
        f_a = a**2 - root
        f_b = b**2 - root
        # midpoint calcs
        t = (a + b) / 2
        f_t = t**2 - root
        # fill trackers
        bisection_tracker.loc[iteration] = [a, b, t, f_a, f_b, f_t]
        # get next points
        if f_t < 0:
            a = t
        else:
            b = t
            
    guess = bisection_tracker.iloc[-2].t
    return bisection_tracker, guess
        

# Newton's Method Algorithm
def newtons_approx(root, x_n, iters = 5):
    newton_tracker = pd.DataFrame(columns = ['x_n', 'f(x)', "f'(x)", 'x_n+1'])
    for iteration in range(iters):
        f = x_n**2 - root
        f_prime = 2 * x_n
        x_n1 = x_n - (f / f_prime)
        newton_tracker.loc[iteration] = [x_n, f, f_prime, x_n1]
        x_n = x_n1
    
    return newton_tracker