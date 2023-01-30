from os import system
import function as fn

names_files = ["bus.txt", "driver.txt", "route.txt"]

info_start = "Выбор операции:"
menu_start = [
    "Вывод автобусов",
    "Добавление автобуса",
    "Вывод водителей",
    "Добавление водителей",
    "Вывод маршрута",
    "Добавление маршрута",
    "Удаление автобуса, водителя, маршрута",
    "Объединить данные 2 файлов в 1",
    "Выход"
]

fn.print_name_files(menu_start, info_start)
answer = input("\nВведите номер: ")

if 0 <= int(answer) < len(menu_start):

    if answer == "0":
        fn.print_file(names_files[0])

    elif answer == "1":
        fn.print_file(names_files[0])
        fn.add_data_file(names_files[0])

    elif answer == "2":
        fn.print_file(names_files[1])

    elif answer == "3":
        fn.print_file(names_files[1])
        fn.add_data_file(names_files[1])

    elif answer == "4":
        fn.print_file(names_files[2])

    elif answer == "5":
        fn.print_file(names_files[2])
        fn.add_data_file(names_files[2])

    elif answer == "6":
        info_start = "Удалить данные в файле:"
        fn.print_name_files(names_files, info_start)
        answer_6 = int(input("\nВведите номер: "))

        if 0 <= answer_6 < len(names_files):
            info_start = "Содержимое файла:"
            work_list = []

            with open(names_files[answer_6], "r", encoding="utf8") as datafile:
                for line in datafile:
                    work_list.append(line)

            fn.print_name_files(work_list, info_start)

            answer_6_1 = int(input("\nВведите номер: "))
            fn.del_data(names_files[answer_6], answer_6_1)

        else:
            print("Данные на вход некорректные")

    elif answer == "7":
        info_start = "Доступные файлы с данными:"
        fn.print_name_files(names_files, info_start)
        answer_7_1 = int(input("\nВведите номер: "))
        answer_7_2 = int(input("\nВведите номер: "))

        if (0 <= answer_7_1 < len(names_files)) and \
           (0 <= answer_7_2 < len(names_files)):

            answer_7_3 = input("\nНазвание файла, по умолчанию формат .txt: ")
            answer_7_3 += ".txt"

            fn.merging_files(names_files[answer_7_1],
                             names_files[answer_7_2],
                             answer_7_3)
        else:
            print("Данные на вход некорректные")
else:
    print("Данные на вход некорректные")
