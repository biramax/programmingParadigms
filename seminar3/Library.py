
class Library:

    def __init__(self):
    # Создаем список для хранения книг
    library = []

    # Функция для добавления книги в библиотеку
    def add_book():
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        book = {"Название": title, "Автор": author}
        library.append(book)
        print("Книга добавлена в библиотеку.")

    # Функция для вывода списка книг в библиотеке
    def display_books():
        if not library:
            print("Библиотека пуста.")
        else:
            print("Список книг в библиотеке:")
            for book in library:
                print(f"Название: {book['Название']}, Автор: {book['Автор']}")