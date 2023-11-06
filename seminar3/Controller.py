
class Controller():

    def run(self):
        # Главный цикл программы
        while True:
            print("\n1. Добавить книгу")
            print("2. Показать список книг")
            print("3. Выйти")
            choice = input("Выберите действие: ")

            if choice == "1":
                add_book()
            elif choice == "2":
                display_books()
            elif choice == "3":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")


