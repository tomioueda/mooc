"""
APlusB.py
By Tomio Ueda

Problem. Given two digits a and b, find a+b.

Input format. The first line of the input contains two integers a and b (separated by a space).
Constraints. 0≤a,b≤9.
Output format. Output a+b.
"""



import sys

input_list = list(map(int, input().split()))

if input_list[0] >= 0:
	if input_list[1] <= 9:
		total = input_list[0] + input_list[1]
		print (total)
	else:
		print ("Second integer is too big: {}".format(input_list[1]))
		sys.exit(1)
else: 
	print ("First integer is too big: {}".format(input_list[0]))
	sys.exit(1)

