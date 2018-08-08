# Copyright 2013 Philip N. Klein
from vec import Vec

def list2vec(L):
    """Given a list L of field elements, return a Vec with domain {0...len(L)-1}
    whose entry i is L[i]

    >>> list2vec([10, 20, 30])
    Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})
    """
    return Vec(set(range(len(L))), {k:L[k] for k in range(len(L))})

def vec2list(v):
    """Given a vector v, return a list L with values of a vector}
        whose entry i is v.f[i]
        
        >>> vec2list(Vec({0, 1, 2},{0: 10, 1: 20, 2: 30}))
        [10, 20, 30]
        """
    return [v.f[k] for k in v.D]


def zero_vec(D):
    """Returns a zero vector with the given domain
    """
    return Vec(D, {})
