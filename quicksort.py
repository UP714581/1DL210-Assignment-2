import assignment2_utils

def quicksort(a):
	if not a:
		return []
	else:
		pivot = a[0]
		less = [x for x in a if x < pivot]
		more = [x for x in a[1:] if x >= pivot]
		return quicksort(less) + [pivot] + quicksort(more)

assignment2_utils.run(quicksort)
