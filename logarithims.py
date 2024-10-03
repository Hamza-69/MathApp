def exp(x):
	if x == 0:
		return 1
	term = 1
	sum = 1
	for i in range(1, 20):
		term *= x / i
		sum += term
	return sum

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
	N = 0
	y = x
	while y>1:
		N += 1
		y /= 2

	return N * ln(2) + ln(y)
