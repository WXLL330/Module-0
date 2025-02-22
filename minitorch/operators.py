"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float) -> float:
    return a*b

def id(x: float) -> float:
    return x

def add(a: float, b: float) -> float:
    return a+b

def neg(x: float) -> float:
    return -x

def lt(a: float, b: float) -> float:
    return a<b

def eq(a: float, b: float) -> float:
    return a==b

def max(a: float, b: float) -> float:
    return a if a > b else b

def is_close(a: float, b: float) -> float:
    return abs(a - b) < 1e-2

def sigmoid(x: float) -> float: 
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))

def relu(x: float) -> float:
    return max(0.0, x)

def log(x):
    return math.log(x)

def exp(x):
    return math.exp(x)

def log_back(x, y):
    return y / x

def inv(x):
    return 1.0 / x

def inv_back(x, y):
    return -y / x**2

def relu_back(x, y):
    if x > 0:
        return y
    else:
        return 0



# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
