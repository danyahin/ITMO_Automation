def first_hw(a: int, b: int) -> None:
    print(max(a, b))


def second_hw(a: int, b: int) -> None:
    if a - b == 135 or a - b == -135:
        print('yes')
    else:
        print('no')


def third_hw(a: int) -> None:
    if a in range(3, 6):
        print('spring')
    elif a in range(6, 9):
        print('summer')
    elif a in range(9, 12):
        print('autumn / fall')
    elif a in range(1, 3) or a == 12:
        print('winter')
    else:
        print('Incorrect month')


def forth_hw(a: int, b: int, c: int) -> None:
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')


# Доп *
def fifth_hw(list_x: list) -> int:
    i = 0
    for elem in list_x:
        if elem > 0:
            i = i + 1
    return i


# print(fifth_hw([1, -2, -3, -4, 0]))
def sixth_hw(years: int, months: int):
    print(years * 365 + months * 29 + years // 4 - years // 100 + years // 400)


# sixth_hw(400,0)
