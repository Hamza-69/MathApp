from logarithims import *
from proprietry import *
def pi():
    sum = 0
    for i in range(1000):
        term = ((-1) ** i) / ((2 * i) + 1)
        sum += term
    sum *= 4
    return sum

def to_radians(angle):
    return (angle / 180) * pi()

def to_degrees(angle):
    return round(angle / pi() * 180, 6)

def principle_value(angle):
    while angle >= 360:
        angle -= 360
    return angle

def sin(x):
    x1 = x
    x = round(principle_value(to_degrees(x)))
    if x == 90:
        return 1
    elif x == -90:
        return -1
    elif x == 30 or x == 150:
        return 1 / 2
    elif x == -30 or x == -150:
        return -1 / 2
    elif x == 180 or x == 0 or x == -180:
        return 0
    term = x1
    sum = term
    for i in range(1, 1000):
        term *= -1 * (x1 ** 2) / (2 * i * (2 * i + 1))
        sum += term
    return sum

def cos(x):
    x1 = x
    x = principle_value(to_degrees(x))
    if x == 0:
        return 1
    elif x == -180 or x == 180:
        return -1
    elif x == 60 or x == -60:
        return 1 / 2
    elif x == 120 or x == -120:
        return -1 / 2
    elif x == 90 or x == -90:
        return 0
    term = 1
    sum = term
    for i in range(1, 1000):
        term *= -1 * (x1 ** 2) / ((2 * i - 1) * (2 * i))
        sum += term
    return sum

def tan(x):
    x1 = x
    x = round(principle_value(to_degrees(x)))
    if x == 90 or x == -90:
        return "Math Error"
    if x == 45 or x == -135:
        return 1
    if x == -45 or x == 135:
        return -1
    return sin(x1) / cos(x1)

def cot(x):
    x1 = x
    x = round(principle_value(to_degrees(x)))
    if x == 0 or x == 180 or x == -180:
        return "Math Error"
    if x == 45 or x == -135:
        return 1
    if x == -45 or x == 135:
        return -1
    return 1 / tan(x1)

def sec(x):
    x1 = x
    x = round(principle_value(to_degrees(x)))
    if x == 90 or x == -90:
        return "Math Error"
    return 1 / cos(x1)

def csc(x):
    x1 = x
    x = round(principle_value(to_degrees(x)))
    if x == 0 or x == 180 or x == -180:
        return "Math Error"
    return 1 / sin(x1)

def arcsin(x):
    if not(-1<= x <= 1):
        return "Math Error"
    if x == 0:
        return 0
    if x == 1:
        return pi()/2
    if x == -1:
        return -pi()/2
    term =  x
    sum = term
    for i in range(1, 500):
        term *= ((x**2)*(2*i - 1)*(2*i))/((2**(2*i))*i**2)
        sum += term/(2*i +1)
    return sum

def arccos(x):
    if not(-1<= x <= 1):
        return "Math Error"
    if x == 0:
        return pi()/2
    if x == 1:
        return 0
    if x == -1:
        return pi()
    return pi()/2 - arcsin(x)

def arctan(x):
    if not(-1<= x <= 1):
        return "Math Error"
    if x == 0:
        return 0
    if x == 1:
        return pi()/4
    if x == -1:
        return -pi()/4
    term = x
    sum = x
    for i in range(1, 1000):
        term *= -1 * x**2
        sum += term/((2 * i) + 1)
    return sum

def arccot(x):
    if not(-1<= x <= 1):
        return "Math Error"
    if x == 0:
        return pi()/2
    if x == 1:
        return pi()/4
    if x == -1:
        return -pi()/4
    return pi()/2 - arctan(x)

def arcsec(x):
    return arccos(1/x)

def arccsc(x):
    return arcsin(1/x)

def cosh(x):
    return (exp(x) + exp(-x) )/2

def sinh(x):
    return (exp(x) - exp(-x) )/2

def tanh(x):
    return sinh(x)/cosh(x)

def coth(x):
    return cosh(x)/sinh(x)

def sech(x):
    return 1/cosh(x)

def csch(x):
    return 1/sinh(x)

def arsinh(x):
    return ln(x + nth_root(x**2 +1,2))

def arcosh(x):
    if not(x>=1):
        return "Math Error"
    return ln(x + nth_root(x**2 - 1,2))

def artanh(x):
    if not (-1<x<1):
        return "Math Error"
    return 0.5*ln((1+x)/(1-x))

def arcoth(x):
    if not(x>1 and x<-1):
        return "Math Error"
    return 0.5*ln((x+1)/(x-1))

def arsech(x):
    if not(0 < x <= 1):
        return "Math Error"
    return ln(1/x + nth_root((1/x**2) - 1,2))

def arcsch(x):
    if x == 0:
        return "Math Error"
    return ln(1/x + nth_root((1/x**2) + 1,2))