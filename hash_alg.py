import string
import datetime


def getHash():
    others = ["@", "#", "_", "-", ".", "/",
              "|", "'", "?", "(", ")", "&", "%", "$", "!", "{", "}", "[", "]", "*", "+"]

    join_chars_nums = []
    abc = string.lowercase[:26]
    abc_upper = abc.upper()
    for i in abc:
        join_chars_nums.append(i)
    for i in range(0, 10):
        join_chars_nums.append(i)
    for i in abc_upper:
        join_chars_nums.append(i)
    for i in others:
        join_chars_nums.append(i)
    return join_chars_nums


def initHash():
    join_chars_nums = getHash()
    index_chars = []
    for index, i in enumerate(join_chars_nums):
        index_chars.append(len(join_chars_nums) - 1 - index)
    new_order = [join_chars_nums[i] for i in index_chars]
    return new_order


def getChar(text):
    join_chars_nums = getHash()
    index_chars = []
    chars = []
    for char in text:
        try:
            int(char)
            num = int(char)
            chars.append(num)
        except ValueError:
            chars.append(char)
    # print chars

    for i in chars:
        for index, j in enumerate(join_chars_nums):
            if i == j:
                index_chars.append(index)

    return index_chars


def hashAlg(text):
    new_order = initHash()
    index_chars = getChar(text)
    hashed_chars = []
    for i in index_chars:
        for index, j in enumerate(new_order):
            if index == i:
                hashed_chars.append(j)
    new_text = "".join(str(x) for x in hashed_chars)
    # print new_text
    return new_text


hashAlg("JAvier123")
