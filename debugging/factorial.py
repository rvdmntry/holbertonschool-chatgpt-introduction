#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

if len(sys.argv) > 1:
	try:
		input_number = int(sys.argv[1])
		if input_number < 0:
			print("Please enter a non-negative integer.")
		else:
			f = factorial(input_number)
			print(f)
	except ValueError:
		print("Please enter a valid integer.")
else:
	print("Usage: script.py <non-negative integer>")
