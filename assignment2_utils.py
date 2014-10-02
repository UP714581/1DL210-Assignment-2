import random
import os
import sys

def test(sorting_algorithm):
	# check if nums.txt exists
	if not os.path.exists('nums.txt'):
		print("No nums.txt found. Creating...")
		os.system('python rangen.py 16')

	# read the content of nums.txt into an array
	nums = open('nums.txt', 'r')
	a = []
	for line in nums:
		a.append(int(str.strip(line)))

	# sort the array using bubblesort
	# You need to change here to call your sorting algorithm
	a = sorting_algorithm(a)

	# output nums_sorted.txt
	nums_sorted = open('nums_sorted.txt', 'w')
	for element in a:
		nums_sorted.write(str(element) + "\n")

	nums.close()
	nums_sorted.close()

	# compare your result (nums_sorted.txt) against the result of bubblesorting algorithm (nums_ref.txt)
	# os.system('sort nums.txt < nums_ref.txt')
	if not os.name == 'posix':
		nums_ref = open('nums_ref.txt', 'w')
		for element in sorted(a):
			nums_ref.write(str(element) + "\n")
		nums_ref.close()
		ret = os.system('FC nums_sorted.txt nums_ref.txt')
	else:
		os.system('sort -n nums.txt > nums_ref.txt')
		ret = os.system('diff nums_sorted.txt nums_ref.txt')

	# output result
	if int(ret) == 0:
		print("Sorted!")

	if int(ret) == 1:
		print("Not sorted!")








