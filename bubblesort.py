#coding: utf-8

import random

def bubblesort(array):
	while True:
		flag = False
		for i in range(0, len(array)-1):
			if array[i] > array[i+1]:
				flag = True
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
		if not flag:
			break

	return array

def main():
	array = []
	for i in range(0, 10):
		array.append(random.randint(0, 20))
	
	print(array)

	bubblesort(array)

	print("\nバブルソート後\n")

	print(array)

	return 0

if __name__ == "__main__":
	main()
