#!/usr/bin/python3
import sys

# Check if any arguments are provided
if len(sys.argv) == 1:
	print("No arguments provided.")
else:
	for index, arg in enumerate(sys.argv):
		print(arg)
