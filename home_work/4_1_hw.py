class Car:

    def __init__(self, color: str = None, type: str = None, year: int = None):
        self.color = color
        self.type = type
        self.year = year

    def engine_start(self):
        print('Автомобиль заведён')

    def engine_stop(self):
        print('Автомобиль заглушен')

    def assign_year(self, year):
        self.year = year

    def assign_type(self, type):
        self.type = type

    def assign_color(self, color):
        self.color = color


ae111 = Car()
ae111.assign_year(1999)
ae111.assign_type('coupe')
ae111.assign_color('turquoise(бирюзовый)')
print(ae111.type, ae111.color, ae111.year)
