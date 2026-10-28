# командна робота: базова версія тімліда (гілка main)
# склад команди:
# тімлід - Дерновий Микита
# розробник 2 - Коваленко Антон

# todo для розробник 2:
# 1) зробити функцію update_phone для зміни номера
# 2) зробити функцію filter_by_operator для пошуку за кодом
# 3) зробити функцію display_operator_statistics для статистики


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
    # видалення контакту
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
    # пошук номера за прізвищем
    surname = surname.strip().capitalize()
    if surname in book:
        print(f"номер для {surname}: {book[surname]}")
    else:
        print(f"контакту {surname} не знайдено")


def find_name_by_phone(book, target_phone):
    # пошук прізвища за номером
    target_phone = target_phone.strip()
    found = [s for s, p in book.items() if p == target_phone]

    if found:
        print(f"номер {target_phone} належить: {', '.join(found)}")
    else:
        print(f"номер {target_phone} не знайдено")


# тут розробник 2 додасть свої функції у гілці feature-improvements
# === НОВІ ФУНКЦІЇ ВІД РОЗРОБНИКА 2 ===
def update_phone(book, surname, new_phone):
    # зміна номера існуючого контакту
    surname = surname.strip().capitalize()
    new_phone = new_phone.strip()
    if not new_phone.isdigit() or len(new_phone) < 10:
        print("номер має містити від 10 цифр")
        return
    try:
        if surname not in book:
            raise KeyError(surname)
        old_phone = book[surname]
        book[surname] = new_phone
        print(f"номер для {surname} змінено: {old_phone} -> {new_phone}")
    except KeyError:
        print(f"помилка: контакту {surname} немає в записнику")
def filter_by_operator(book, code):
    # пошук за кодом оператора
    code = code.strip()
    matches = {s: p for s, p in book.items() if p.startswith(code)}
    if matches:
        print(f"\nконтакти з кодом {code} ({len(matches)} знайдено):")
        for s, p in sorted(matches.items()):
            print(f"{s}: {p}")
    else:
        print(f"контактів з кодом {code} не знайдено")
def display_operator_statistics(book):
    # статистика операторів
    if not book:
        print("\nзаписник порожній")
        return
    operators = {
        "Vodafone (050, 066, 095, 099)": ("050", "066", "095", "099"),
        "Київстар (067, 068, 096, 097, 098)": ("067", "068", "096", "097", "098"),
        "lifecell (063, 073, 093)": ("063", "073", "093"),
    }
    stats = {name: 0 for name in operators}
    stats["інші"] = 0
    for phone in book.values():
        matched = False
        for op, prefixes in operators.items():
            if phone.startswith(prefixes):
                stats[op] += 1
                matched = True
                break
        if not matched:
            stats["інші"] += 1
    print("\nстатистика по операторах:")
    print(f"всього контактів: {len(book)}")
    for op, count in stats.items():
        pct = (count / len(book)) * 100 if book else 0
        print(f"- {op}: {count} ({pct:.0f}%)")

def main():
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
        print("\nкомандний проєкт (базова версія v1):")
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
