def nth_root(x,n):
    if n%2 == 0 and x < 0:
        return "Math Error"
    return x**(1/n)