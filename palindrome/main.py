

def is_palindrome(phrase : str):
	pass


def palindromify(phrase : str):
	pass


if __name__ == '__main__':

	phr_1 = 'lololololol'
	phr_2 = 'lololololololo'
	phr_3 = 'Able was I ere I saw Elba'
	phr_4 = 'A Santa at NASA'
	phr_5 = 'A nut is a jar of tuna'


	assert(is_palindrome(phr_1))
	assert(not is_palindrome(phr_2))
	assert(is_palindrome(phr_3))
	assert(is_palindrome(phr_4))
	assert(not is_palindrome(phr_5))