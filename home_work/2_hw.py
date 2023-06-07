def task_1() -> None:
    q: int = 0
    w: float = 1.41421356237
    x: str = 'Как дела?'
    y: list = ['malchiki', 'devochki', 'tantcooyut', 'pod', 'tekhno']
    z: bool = False
    print('q type is ', type(q), '\nw type is ', type(w), '\nx type is ', type(x), '\ny type is ', type(y), '\nz type is ', type(z))


# def task_1_1() -> str:
#     q: int = 0
#     w: float = 1.41421356237
#     x: str = 'Как дела?'
#     y: list = ['malchiki', 'devochki', 'tantcooyut', 'pod', 'tekhno']
#     z: bool = False
#     f = 'q type is '+type(q)+'\nw type is '+type(w)+'\nx type is '+type(x)+'\ny type is '+type(y)+'\nz type is '+type(z)
#     return f


def task_1_2() -> list:
    q: int = 0
    w: float = 1.41421356237
    x: str = 'Как дела?'
    y: list = ['malchiki', 'devochki', 'tantcooyut', 'pod', 'tekhno']
    z: bool = False
    return [type(q), type(w), type(x), type(y), type(z)]


task_1()
# print(task_1_1())
# print(task_1_2())


def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])


task_2()


def task_3(a: int) -> int:
    return a**2


print(task_3(16))
