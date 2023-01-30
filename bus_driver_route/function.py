# def read_data_from_file(name):
#     result = []
#     with open(name, "r", encoding="utf8") as datafile:
#         for line in datafile:
#             result.append(line.strip("\n").split(","))
#     return result

'''===============================Вывод меню================================'''


def print_name_files(list_name_file: list, info_user: str):
    print("\n", info_user, sep="")

    for i in range(len(list_name_file)):
        print("{} - {}".format(i, list_name_file[i]))


'''========================================================================='''

'''========================Добавление данных в файл========================='''


def save_data_to_file(name, data_list):
    with open(name, "a", encoding="utf8") as datafile:
        datafile.write(data_list + "\n")


def add_data_file(name):
    new_data = (input("Введите данные: "))
    save_data_to_file(name, new_data)


'''========================================================================='''

'''========================Вывод данных из файла============================'''


def print_file(file_name: str):
    print("\n", "Данные файла: {}".format(file_name), sep="")

    with open(file_name, "r", encoding="utf8") as datafile:
        for line in datafile:
            print(line, end="")


'''========================================================================='''

'''=============================Удаление данных============================='''

# потом переделать убрать дубли del_data, merging_files


def del_data(file_name: str, del_line: int):

    new_data = []

    with open(file_name, "r", encoding="utf8") as datafile:

        for line in datafile:
            new_data.append(line)

    with open(file_name, "w", encoding="utf8") as datafile:
        new_data.pop(del_line)

        for line in new_data:
            datafile.write(line)


'''========================================================================='''

'''====================Объединение данных -> Общий файл====================='''

# потом переделать убрать дубли del_data, merging_files


def merging_files(file_name_1: str, file_name_2: str, new_file: str):
    data_file_1 = []
    data_file_2 = []

    with open(file_name_1, "r", encoding="utf8") as datafile:

        for line in datafile:
            data_file_1.append(line)

    with open(file_name_2, "r", encoding="utf8") as datafile:

        for line in datafile:
            data_file_2.append(line)

    with open(new_file, "w", encoding="utf8") as datafile:
        for line in data_file_1:
            datafile.write(line)

        for line in data_file_2:
            datafile.write(line)


'''========================================================================='''

#  реализовать функцию объядинения данных файлов

# print_bus()

# del_data("bus.txt", 2)

# merging_files("bus.txt", "driver.txt", "result.txt")
