def exp(x):
	if x == 0:
		return 1
	term = 1
	sum = 1
	for i in range(1, 20):
		term *= x / i
		sum += term
	return sum

def exp_base(x,b):
	return b**x

def ln(x):
	if x <=0:
		return "Math Error"
	elif x == 1:
		return 0
	elif 0 < x <= 2:
		x = x - 1
		term = x
		sum = term
		for i in range(2, 1000):
			term *= -1 * x
			sum += term / i
		return sum
	n = 0
	y = x
	while y>1:
		n += 1
		y /= 2

	return n * ln(2) + ln(y)
def log(x,b):
	if b == x:
		return 1
	elif x == 1:
		return 0
	elif b <= 1:
		return "Math Error"
	x_copy = x
	n = 0
	while x_copy % b == 0:
		n += 1
		x_copy /= b
	return	n + ln(x_copy)/ln(b)