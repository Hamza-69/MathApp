def pi():
    sum = 0
    for i in range(20):
        term = ((-1)**i) / ((2*i)+1)
        sum += term
    sum *= 4
    return pi
def to_radians(angle):
    return (angle/180)*pi
def to_degrees(angle):
    return (angle/pi)*180
def principle_value(angle):
    while angle >= 360:
        angle -= 360
    return angle
def sin(x):
    x = principle_value(x)
    if x == 90:
        return 1
    elif x == -90:
        return -1
    elif x == 30 or x == 150:
        return 1/2
    elif x == -30 or x == -150:
        return -1/2
    elif x == 180 or x == 0 or x == -180:
        return 0
    term = x
    sum = term
    for i in range(1,20):
        term *= -1*(x**2)/(2*i*(2*i+1))
        sum += term
    return sum
def cos(x):
    x = principle_value(x)
    if x == 0:
        return 1
    elif x == -180 or x==180:
        return -1
    elif x == 60 or x == -60:
        return 1 / 2
    elif x == 120 or x == -120:
        return -1 / 2
    elif x == 90 or x == -90:
        return 0
    term = 1
    sum = term
    for i in range(1,20):
        term *= -1*(x**2)/(2*i - 1)(2*i)
        sum += term
    return sum
def tan(x):
    if x == 90 or x == -90:
        print("Math Error")
    x = principle_value(x)
    return sin(x)/cos(x)
def cot(x):
    if x == 0 or x == 180 or x == -180:
        print("Math Error")
    x = principle_value(x)
    return 1/tan(x)
def sec(x):
    if x == 90 or x == -90:
        print("Math Error")
    x = principle_value(x)
    return 1/cos(x)
def csc(x):
    if x == 0 or x == 180 or x == -180:
        print("Math Error")
    x = principle_value(x)
    return 1/sin(x)
