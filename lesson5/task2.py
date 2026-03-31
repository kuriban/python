import string

myRow = input('Row: ')

def to_hashTag(row: str) -> str:
    clearrow = ''.join(ch for ch in row if ch not in string.punctuation)

    hashtag = '#' + ''.join(word.capitalize() for word in clearrow.split())

    return hashtag[:140]

print(to_hashTag(myRow))