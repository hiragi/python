#coding: utf-8

def prime1():
	counter = 0
	primes = []

	for n in range(2, 1001):
		isprime = True
		for i in range(2, n):
			counter += 1
			if n % i == 0:
				isprime = False
				break

		if isprime:
			primes.append(n)
	
	print(primes)
	print(len(primes))
	print(u"除算を行った回数：%d" % counter)

prime1()
