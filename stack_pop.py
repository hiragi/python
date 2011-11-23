#coding: utf-8
import sys

def main():
	stack = []

	while(True):
		print "現在のスタック："
		print(stack)

		r = input("\n1:Push\n2:Pop\nOthers:Exit\n>")

		if r == 1:
			x = input("What is your stack number?")
			stack.append(x)
		elif r == 2:
			print("%dをとりだした" %stack.pop())
		else:
			sys.exit()


if __name__ == "__main__":
	main()
