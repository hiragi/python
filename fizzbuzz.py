# fizz:3 buzz:5 fizzbuzz:15

FIZZ = 3
BUZZ = 5
FIZZBUZZ = 15

for i in range(0, 101):
	if i == 0:
		print i
	elif i % FIZZBUZZ == 0:
		print "fizzbuzz"
	elif i % FIZZ == 0:
		print "fizz"
	elif i % BUZZ == 0:
		print "buzz"
	else:
		print i
