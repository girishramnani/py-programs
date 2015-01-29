__author__ = 'Girish'

import math

import scipy.odr

def func(x):
    return math.exp(-x)-x

def secant(func,lower,upper):
    def secant_func(func , xi,xi_1):
