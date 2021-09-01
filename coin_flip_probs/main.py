import numpy as np

def exact_successes(nflips: int, nheads: int) -> float:
	""" Returns the probabiliy of nheads out of nflips exactly """
	pass


def at_least_successes(nflips: int, nheads: int) -> float:
	""" Returns the probabiliy of at least nheads out of nflips """
	pass

if __name__ == '__main__':

	print(exact_successes(10, 3))
	print(at_least_successes(10, 3))