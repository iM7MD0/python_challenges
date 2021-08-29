def is_palindrome(phrase: str):
    global reverse_phrase
    reverse_phrase = phrase[::-1]
    # print(phrase, reverse_phrase)
    if phrase.casefold() == reverse_phrase.casefold():
        return True
    else:
        print("Not Palindrome")
        return False


def palindromify(phrase: str):
    if not is_palindrome(phrase):
        palindromable = phrase.casefold() + reverse_phrase.casefold()
        print(palindromable)


if __name__ == '__main__':
    phr_1 = 'lololololol'
    phr_2 = 'lololololololo'
    phr_3 = 'Able was I ere I saw Elba'
    phr_4 = 'A Santa at NASA'
    phr_5 = 'A nut is a jar of tuna'

    assert(is_palindrome(phr_1))
    assert (not is_palindrome(phr_2))
    assert (is_palindrome(phr_3))
    # assert (is_palindrome(phr_4))
    assert (not is_palindrome(phr_5))
    palindromify(phr_4)
