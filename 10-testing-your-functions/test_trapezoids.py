from trapezoids import trapezint

def hat(x):
    """Simple function that equals x between [0,1], 2-x between [1,2], 0 otherwise"""
    if 0 <= x <= 1:
        return x
    elif 1 <= x <=2:
        return 2-x
    return 0

def test_trapezint_hat04():
    """Can we integrate a step function from 0 to 4 with four trapezoids?"""
    result = trapezint(hat, 0, 4)
    assert result == 1 #if function is working, result should be 1

def test_trapezint_hat01():
    """Can we integrate a step function from 0 to 1 with one trapezoid?"""
    result = trapezint(hat, 0, 1)
    assert result == 0.5

def test_trapezint_sin0pi():
    import numpy as np
    
    result = trapezint(np.sin, 0, np.pi, n=2)
    assert abs(result - (np.pi / 2)) < 1e-5

