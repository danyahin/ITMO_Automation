from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


class Link(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


search = Input('Muhosransk', "Вы в Мухосранске")
button_1 = Button('On page', "Кнопка на странице")
title_1 = Title('On the header', "Шапка страницы")
link_1 = Link('On the page or in the button', "Ссылка")
# print(search.text + ' -- ' + search.loc + '\n')
# print(button_1.text + ' -- ' + button_1.loc + '\n')
# print(title_1.text + ' -- ' + title_1.loc + '\n')
# print(link_1.text + ' -- ' + link_1.loc + '\n')
print(search.check_text())
print(button_1.check_text())
print(title_1.check_text())
print(link_1.check_text())
