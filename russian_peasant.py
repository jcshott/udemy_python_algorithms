def russian_peasant_multiplication(num1, num2):
	""" My initial solution"""

	# these actually don't need to be max & min, works either way.
	divide_num = max(num1, num2)
	multiply_num = min(num1, num2)
	div_list = [divide_num]
	mult_list = [multiply_num]

	while divide_num > 1:
		div_list.append(divide_num/2)
		mult_list.append(multiply_num*2)
		divide_num = divide_num/2
		multiply_num = multiply_num*2

	for idx, num in enumerate(div_list):
		if num % 2 == 0:
			mult_list[idx] = 0

	return sum(mult_list)

print russian_peasant_multiplication(24, 16)
print russian_peasant_multiplication(53, 12)

def russian(a, b):
	""" more effecient way per video"""

	# assign a (divide column) & b (multiply column) to variables

	x = a
	y = b

	# establish a counter to hold our sum
	z = 0

	# once x is less than one we want to stop and return our sum
	while x > 0:
		# since we only add the y var value when x is odd, we can just check for that
		if x % 2 == 1:
			z += y
		# divide/multiply our variables
		x /= 2
		y *= 2
	
	return z

print russian(24, 16)
print russian(16, 24)
print russian(53, 12)


