def add(x, y):
    return x+y


def arg(a, b, c=[1, 1, 1], d=3):
    return c


def range_arg(a, b, c, d):
    return a+' '+b+' '+c+' '+d


def first_of_tuple(a=(1, 2, 3, 4)):
    return a[0]


def circle_area(radius, pi=3.141592653589793):
    return pi*radius**2


def indent(s: str, width: int) -> str:
    return ' '*(max(0, width - len(s))) + s


def string_length(s: str = '') -> int:
    return len(s)


def the_longest_one(x: list, y: list) -> int:
    return max(len(x), len(y))


def list_append(x: list):
    x.append(5)
    return x


def list_sum(x: list):
    sum: int = 0
    for i in x:
        sum = sum + i
    return sum


# print(add(1, 2))
# print(add('I a', 'm a tester'))
# print(arg(1, 1, 1, 1))
# print(arg(2, 2))
# print(arg(2, 2, d=1))
#print(range_arg('1', '2', d='3', c='4'))
# print(first_of_tuple(('fuck you', 'goddam')))
# print(circle_area(2,3))
# print(string_length('12345'))
# print(the_longest_one([1, 2, 3, 4, 5, 6], [2, 3, 9]))
# print(list_append([1, 2, 3]))
# print(list_sum([1, 2, 3, 4]))
x = indent('12345', 123)
y: int = 0
i: int = 0
while x[i] == ' ':
    y = y + 1
    i = i + 1
print(y)
