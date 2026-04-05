def seconds_to_time(total_seconds):
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if 11 <= days % 100 <= 14:
        day_word = "днів"
    elif days % 10 == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    h = str(hours).zfill(2)
    m = str(minutes).zfill(2)
    s = str(seconds).zfill(2)

    return f"{days} {day_word} {h}:{m}:{s}"


n = int(input("Введіть кількість секунд: "))
print(seconds_to_time(n))