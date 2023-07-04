def get_trcky_word_revers(word: str) -> str:
    """
    Get a string in which all alpha-characters change their order to the reverse,
    and all other characters take the same places.

    >>> a = 'abcd'
    >>> get_trcky_word_revers(a)
    'dcba'

    >>> b = '1ds 34 asdf '
    >>> get_trcky_word_revers(b)
    '1fd 34 sasd '
    """
    # get list only for letters
    alpha_list = [symbol for symbol in word if symbol.isalpha()]
    # get reversed alpha_lisr
    alpha_list.reverse()
    # get result list wis inverted alpha string and exising non-alpha string
    result_list = [alpha_list.pop(0) if symbol.isalpha() else symbol for symbol in word]
    # get result string (use [str.join()](https://docs.python.org/3/library/stdtypes.html#str.join))
    return "".join(result_list)


def tricky_invert_sentence(original_sentence: str) -> str:
    """Get a sentence that consists of the words of the input sentence in the same order,
    but each word is obtained by reversing all alpha-characters within the word, while leaving
    all other characters in their places.

    >>> a = 'asdf 1g?zxcv56  1we'
    >>> tricky_invert_sentence(a)
    'fdsa 1v?cxzg56 1ew'

    """

    return " ".join([get_trcky_word_revers(word) for word in original_sentence.split()])


if __name__ == "__main__":
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]

    for text, reversed_text in cases:
        assert tricky_invert_sentence(text) == reversed_text
