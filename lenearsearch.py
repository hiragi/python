import random
import sys

def lsearch(array, x):
	i = 0
	while True:
		if i > len(array)-1:
			break

		if array[i] == int(x):
			break

		if array[i] != int(x):
			i += 1

	if i < len(array):
		return i
	
	return None

def main():
	array = []
	for i in range(0, 10):
		array.append(random.randint(0, 20))
		print "[%i]:" % i,
		print array[i],
	
	print("")
	x = raw_input("What is your search number?:")

	r = lsearch(array, x)

	if r == None:
		print("Not found")
	else:
		print("Your search number is here %i" %r)


if __name__ == "__main__":
	main()
