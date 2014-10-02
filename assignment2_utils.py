import random
import os
import sys

def run(sorting_algorithm):
	nums = open('nums.txt', 'r')
	a = [int(str.strip(line)) for line in nums]
	nums.close()

	result = sorting_algorithm(a)

	nums_sorted = open('nums_sorted.txt', 'w')
	for element in result:
		nums_sorted.write(str(element) + '\n')
	nums_sorted.close() 

	compare_with_bubblesort(a)

def compare_with_bubblesort(unsorted_list):
	nums_ref = open('nums_ref.txt', 'w')
	for element in bubblesort(unsorted_list):
		nums_ref.write(str(element) + '\n')
	nums_ref.close()

	command = 'diff' if os.name == 'posix' else 'FC'

	ret = os.system(str.format('{0} nums_sorted.txt nums_ref.txt', command))

	print('Sorted!' if int(ret) == 0 else 'Not Sorted!')

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False
    return a







