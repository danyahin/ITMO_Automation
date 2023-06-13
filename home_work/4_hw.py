class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


one = Rectangle(5, 8)
print(one.area(), one.perimeter())
two = Rectangle(1, 2)
print(two.area(), two.perimeter())
abcd = Rectangle(1, 8)
print(abcd.area(), abcd.perimeter())


class Math:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


class Button_QA:

    def __init__(self, text, type='Кнопка', loc=''):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return 'Клик по кнопке {}'.format(self.text)


Text_box_button = Button_QA('Text Box')
print(Text_box_button.text)
print(Text_box_button.click())
Check_box_button = Button_QA('Check Box')
print(Check_box_button.text)
print(Check_box_button.click())
Radio_button = Button_QA('Radio Button')
print(Radio_button.text)
print(Radio_button.click())
Web_tables_button = Button_QA('Web Tables')
print(Web_tables_button.text)
print(Web_tables_button.click())
Buttons_button = Button_QA('Buttons')
print(Buttons_button.text)
print(Buttons_button.click())
Links_button = Button_QA('Links')
print(Links_button.text)
print(Links_button.click())
Br_links_button = Button_QA('Broken Links - Images')
print(Br_links_button.text)
print(Br_links_button.click())
Loads_button = Button_QA('Upload and Download')
print(Loads_button.text)
print(Loads_button.click())
Dynamic_properties_button = Button_QA('Dynamic Properties')
print(Dynamic_properties_button.text)
print(Dynamic_properties_button.click())
