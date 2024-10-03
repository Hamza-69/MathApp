def factorial(n):
    if n <0:
        return "Math Error"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def combination(n, r):
    if  n>r:
        return "Math Error"
    return factorial(n)/(factorial(r)*factorial(n-r))
def permutation(n, r):
    if  n>r:
        return "Math Error"
    return factorial(n)/factorial(n-r)