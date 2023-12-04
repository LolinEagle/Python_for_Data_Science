import sys
from ft_filter import ft_filter

def main():
	# Exception
	if (len(sys.argv) < 3):
		return (0)
	try:
		if (len(sys.argv) != 3):
			raise AssertionError("AssertionError: more than two argument is provided")

		# Code
		ft_list = []
		tmp = ""

		for i in sys.argv[1]:
			if (i == ' '):
				ft_list += tmp
				tmp = ""
				continue
			tmp += i

		print(ft_list)
		try:
			print(int(sys.argv[2]))
		except ValueError:
			raise AssertionError("AssertionError: argument is not an integer")
	except AssertionError as msg:
		print(msg)
		return (1)

if __name__ == "__main__":
	main()