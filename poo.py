class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, ni nombre es {self.name} y tengo {self.age}")


person1 = Person("Ana",30)
person2 = Person("Luis",25)

#person1.greet()
#person2.greet()

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposito(self, amount):
        if self.is_active:
            self.balance += amount
            print((f"Se ha depositado {amount}. saldo actual {self.balance}"))
        else:
            print("No se puede depositar, cuenta inactiva")

    def withdraw(self,amount):
        if self.active:
            if amount<= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual es igual a {self.balance}")

    def desactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print(f"la cuenta ha sido activada")

account1 = BankAccount("Ana",500)
account2 = BankAccount("Luuis",1000)

#llamada a los métodos

#account1.deposito(200)
#account2.deposito(100)
#account1.desactivate_account()
#account1.deposito(50)
#account1.activate_account()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")

class User:
    def __init__(self,name,user_id):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = []
        
    def borrow_book(self,book):
        if book.available:
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no esta disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"El libro {book.title} a sido devuelto")
        else:
            print(f"El libro {book.title} no esta en la lista de prestados")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado")

    def register_user(self,user):
        self.users.append(user)
        print(f"el usuario {user.name} ha sido registarado")

    def show_available_books(self):
        print("Los libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

book1 = Book("el principito","antoine")
book2 = Book("1984","george orwell")

#Crear usuario
user1 = User("Carli","001")

#Crear biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#Mostrar libros
library.show_available_books()

#Realizar prestamo
user1.borrow_book(book1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_available_books()

