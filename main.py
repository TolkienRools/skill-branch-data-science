import copy

def part_deriv(arg, f, index):
    d_x = 0.0000001
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
