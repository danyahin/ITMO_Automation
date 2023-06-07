num = 2147483648

if num:
    print('Число положительное')
elif num == 0:
    print('Число равно нулю')
else:
    print('Число отрицательное')


def assembled(str_1: str = 'test', str_2: str = 'test1') -> None:
    # if str_2[0:len(str_1)] == str_1:
    #     print('ДА')
    # else:
    #     print('НЕТ')
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')


assembled()

permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


def vysshee_obrazovanie(x:int = -1) -> None:
    if x>=1 and x<=4:
        print('бакалавр')
    elif x>=5 and x<=6:
        print('магистр')
    elif x>=7 and x<=9:
        print('аспирант')
    elif x==0:
        print('У тебя нет высшего образования')
    elif x==10:
        print('Ты в медицинском')
    else:
        print('Введите корректный год обучения')


vysshee_obrazovanie()


def plus_minus(x) -> None:
    if 100<x or -100>x:
        print('-')
    else:
        print('+')


plus_minus(99)
