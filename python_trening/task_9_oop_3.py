class Soda:
    def __init__(self, taste: str = None):
        self.taste = taste

    def show_my_drink(self):
        if self.taste is None:
            print('Обычная газировка')
        else:
            print('Газировка и {}'.format(self.taste))


obj_1 = Soda('малина')
obj_2 = Soda()
obj_1.show_my_drink()
obj_2.show_my_drink()
