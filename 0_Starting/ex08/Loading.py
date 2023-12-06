import sys
import os

def ft_tqdm(lst: range) -> None:
	"""def ft_tqdm(lst: range) -> None:\nCopy the function tqdm with the yield operator"""
	length = len(lst)								# Length of the argument
	term_w = os.get_terminal_size(1).columns - 40	# Get size of terminal width

	for i, item in enumerate(lst):
		progress = (i + 1) / length
		bar = '█' * int(term_w * progress)
		space = ' ' * int(term_w - len(bar))

		sys.stdout.write(f"\r{int(progress * 100):>3}%|{bar}{space}| {i + 1}/{length}")
		sys.stdout.flush()	# Force writing in standard output
		yield item			# Suspends execution and return value back
	print()
