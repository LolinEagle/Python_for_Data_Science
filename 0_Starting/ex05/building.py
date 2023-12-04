import sys

def main():
	if (len(sys.argv) < 2):
		return (0)
	char = 0
	upper = 0
	lower = 0
	marks = 0
	spaces = 0
	digits = 0

	try:
		if (len(sys.argv) != 2):
			raise AssertionError("AssertionError: more than one argument is provided")
	except AssertionError as msg:
		print(msg)
		return (1)
	for i in sys.argv[1]:
		char += 1
		if (i.isupper()):
			upper += 1
		elif (i.islower()):
			lower += 1
		elif (i.isspace()):
			spaces += 1
		elif (i.isdecimal()):
			digits += 1
		else:
			for j in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
				if (i == j):
					marks += 1
	print(f"The text contains {char} characters:\n{upper} upper letters\n{lower} lower letters\n{marks} punctuation marks\n{spaces} spaces\n{digits} digits")

if __name__ == "__main__":
	main()
