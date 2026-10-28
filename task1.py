# телефонний довідник (варіант 5)


def display_all(book):
    # вивід усіх контактів
    if not book:
        print("\nзаписник порожній")
        return

    print(f"\nсписок контактів ({len(book)} осіб):")
    for surname, phone in book.items():
        print(f"{surname}: {phone}")


def add_entry(book, surname, phone):
    # додавання контакту
    surname = surname.strip().capitalize()
    phone = phone.strip()

    if not surname:
        print("прізвище не може бути порожнім")
        return

    if not phone.isdigit() or len(phone) < 10:
        print("номер має містити від 10 цифр")
        return

    if surname in book:
        print(f"контакт {surname} оновлено")
    else:
        print(f"контакт {surname} додано")

    book[surname] = phone


def delete_entry(book, surname):
    # видалення контакту з обробкою помилки
    surname = surname.strip().capitalize()
    try:
        del book[surname]
        print(f"контакт {surname} видалено")
    except KeyError:
        print(f"помилка: контакту {surname} немає в записнику")


def display_sorted(book):
    # сортування за алфавітом
    if not book:
        print("\nзаписник порожній")
        return

    print("\nконтакти за алфавітом:")
    for surname in sorted(book):
        print(f"{surname}: {book[surname]}")


def find_phone_by_name(book, surname):
    # пошук номера за прізвищем (п. а)
    surname = surname.strip().capitalize()
    if surname in book:
        print(f"номер для {surname}: {book[surname]}")
    else:
        print(f"контакту {surname} не знайдено")


def find_name_by_phone(book, target_phone):
    # пошук прізвища за номером (п. б)
    target_phone = target_phone.strip()
    found = [s for s, p in book.items() if p == target_phone]

    if found:
        print(f"номер {target_phone} належить: {', '.join(found)}")
    else:
        print(f"номер {target_phone} не знайдено")


def main():
    # початковий словник на 10 осіб
    phonebook = {
        "Коваленко": "0501234567",
        "Шевченко": "0672345678",
        "Бондаренко": "0633456789",
        "Мельник": "0954567890",
        "Ткаченко": "0975678901",
        "Кравченко": "0506789012",
        "Олійник": "0687890123",
        "Поліщук": "0938901234",
        "Лисенко": "0669012345",
        "Дерновий": "0990123456",
    }

    while True:
        print("\nменю телефонного записника:")
        print("1 - показати всі контакти")
        print("2 - знайти телефон за прізвищем")
        print("3 - знайти прізвище за номером")
        print("4 - додати контакт")
        print("5 - видалити контакт")
        print("6 - сортувати за алфавітом")
        print("0 - вихід")

        choice = input("оберіть дію: ").strip()

        if choice == "1":
            display_all(phonebook)
        elif choice == "2":
            surname = input("введіть прізвище: ")
            find_phone_by_name(phonebook, surname)
        elif choice == "3":
            phone = input("введіть номер: ")
            find_name_by_phone(phonebook, phone)
        elif choice == "4":
            surname = input("введіть прізвище: ")
            phone = input("введіть номер: ")
            add_entry(phonebook, surname, phone)
        elif choice == "5":
            surname = input("введіть прізвище: ")
            delete_entry(phonebook, surname)
        elif choice == "6":
            display_sorted(phonebook)
        elif choice == "0":
            print("роботу завершено")
            break
        else:
            print("невірний вибір, спробуйте ще раз")


if __name__ == "__main__":
    main()
