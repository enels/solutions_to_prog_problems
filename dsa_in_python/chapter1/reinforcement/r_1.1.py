def is_multiple(n, m):
	# start from 2 since 0 will lead to infinite loop
	# and 1 will always lead to True
	i = 2;
	while True:	
		if n == m * i:
			return True
		# m * i gone beyond n
		elif n < m * i:
			return False
		i += 1;

	# reached the end of range means n not a multiple of m
	return False
