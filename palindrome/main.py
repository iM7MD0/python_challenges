def is_palindrome(phrase: str):
    global reverse_phrase
    reverse_phrase = phrase[::-1]
    if phrase.casefold() == reverse_phrase.casefold():
        return True
    else:
        return False


def palindromify(phrase: str):
    if not is_palindrome(phrase):
        palindromable = phrase.casefold() + reverse_phrase.casefold()
        return palindromable
    return phrase


def find_longest_palindrome(phrase: str):
    pass


if __name__ == '__main__':
    phr_1 = 'lololololol'
    phr_2 = 'lololololololo'
    phr_3 = 'Able was I ere I saw Elba'
    phr_4 = 'A Santa at NASA'
    phr_5 = 'A nut is a jar of tuna'

    assert (is_palindrome(phr_1))
    assert (not is_palindrome(phr_2))
    assert (is_palindrome(phr_3))
    assert (is_palindrome(phr_4))
    assert (not is_palindrome(phr_5))

    print(palindromify(phr_1))
    print(palindromify(phr_2))
    print(palindromify(phr_3))
    print(palindromify(phr_4))
    print(palindromify(phr_5))
