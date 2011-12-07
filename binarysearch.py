import random
import sys

def binarysearch(array, x, left, right):
	while(left < right):
		mid = (left+right)/2
		if x > array[mid]:
			left = mid+1
		else:
			right = mid
		if array[left] == x:
			return left

	return None

def main():
	array = [random.randint(0, 20) for i in range(0, 10)]
	array.sort()
	print(array)
	
	x = input("What is your search number?")
	r = binarysearch(array, x, 0, len(array))

	if r == None:
		print("Your search number is not found")
	else:
		print("Your search number is here %d" %r)

if __name__ == "__main__":
	main()
