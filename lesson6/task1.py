import string


def between_letters(s):
    letters = string.ascii_letters
    start, end = s.split('-')

    i = letters.index(start)
    j = letters.index(end)

    result = ''
    while i <= j:
        result += letters[i]
        i += 1

    return result

row = input('Вводить через дефіс дві літери:')

print(between_letters(row))