import keyword
import string

def check_row(row: str) -> bool:
    badSymbols = set(string.punctuation + ' ') - {'_'}
    if '__' in row:
        print("Не повино складатись не більш чим з одного нижнього підкреслення подряд" "False")
        return False

    if keyword.iskeyword(row):
        print("Змінна не може бути жодним із зареєстрованих слів.." "False")
        return False
    if row[0].isdigit():
        print("не може починатися з цифри." "False")
        return False

    for i in row:
        if i.isupper():
            print("не може містити великі літери" "False")
            return False

        if i in badSymbols:
            print("не може містити пробіл і знаки пунктуації ", "False")
            return False

    print("TRUE")
    return True

strRow = input("Ім'я змінної: ")

check_row(strRow)
