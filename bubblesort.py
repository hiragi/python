def bubblesort(array):
	while True:
		flag = False
		for i in range(0, len(array)-1):
			if array[i] > array[i+1]:
				flag = True
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
		if flag == False:
			break

	return array

test = [2, 4, 7, 1, 3, 9, 8, 6, 5]
bubblesort(test)

print test
