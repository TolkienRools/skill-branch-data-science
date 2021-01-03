import copy
import numpy as np

def part_deriv(arg, f, index):
    d_x = 0.00001
    tmp = copy.copy(arg)
    tmp[index] += d_x
    return round(((f(tmp) - f(arg)) / d_x),2)


def derivation(x, f):
    d_x = 0.0000001
    return round(((f(x + d_x) - f(x)) / d_x),2)


def gradient(arg, f):
    grad = []

    for i in range(len(arg)):
        grad.append(part_deriv(arg, f, i))

    return grad


def gradient_optimization_one_dim(f):
    epsilon = 0.001
    x = 10
    for i in range(50):
        x -= epsilon * derivation(x,f)
    return round(x, 2)


def gradient_optimization_multi_dim(f):
    epsilon = 0.001
    arg = np.array([4,10], dtype=float)
    for i in range(50):
        arg -= epsilon * np.array(gradient(arg,f))
    return arg.round(2)