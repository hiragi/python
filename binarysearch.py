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

	return -1

def main():
	array = [0] * 8
	array[0] = random.randint(0, 20)
	print("[0]:%d" % array[0])
	for i in range (1, len(array)):
		array[i] = array[i-1] + random.randint(0, 20)
		print("[%d]:%d" %(i, array[i]))
	
	x = input("What is your search number?")
	r = binarysearch(array, x, 0, len(array))

	if r == -1:
		print("Your search number is not found")
	else:
		print("Your search number is here %d" %r)

if __name__ == "__main__":
	main()
