def derivation(x, f):
    d_x = 0.001
    return round(((f(x + d_x) - f(x)) / d_x),2)