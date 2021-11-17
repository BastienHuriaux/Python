
def fact(n):
    """
    Retourne la factorielle de n.

    Args:
        n: valeur entière >= 2

    Returns:
        fact(n) : n*(n-1)* ... * 2

    >>> fact(-1)
    'n must be strictly positive'
    >>> fact(0)
    'n must be strictly positive'
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(5)
    120
    >>> fact(10)
    3628800
    """
    if n <= 0:
        return 'n must be strictly positive'
    if n <= 2:
        return n
    return n*fact(n-1)