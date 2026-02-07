class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}!')

    def __dict__(self):
        return {'name': self.name, 'age': self.age}

person1 = Person("Glyzel Galagar", 18)
person2 = Person("Haruto Kurosaki", 21)
person3 = Person("Jake Kuro", 19)

person1.greet()
person2.greet()
person3.greet()
print(person1.__dict__())

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print('Get Started!')

    def __getattr__(self, item):
        return f'{self.brand} {self.model}'

cars = [Car('suzuki','dfs'), Car('samsung','ddd')]
for car in cars:
    car.start()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, name: str):
        for book in self.books:
            if book.title == name:
                self.books.remove(book)
                break
    def display_all_books(self):
        [print(x.title) for x in self.books]

library = Library()
book1 = Book("Java Programming", "Glyzel Galagar")
library.add_book(book1)
library.display_all_books()