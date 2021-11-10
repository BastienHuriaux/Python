#ex4.py
def est_premier(n):
    """
    Retourne si un nombre est premier

    Args:
        n: valeur entière positive
    
    Returns:
        True ou false

    >>> est_premier(10)
    False
    >>> est_premier(11)
    True
    """
    a = int(pow(n,0.5))
    for i in range(2,a+1):
        if(n%i == 0):
            return False
    else:
        return True
