# imports
import random, time, csv

# connect to files
reg_status_set = open("reg.txt", "w")
reg_status_get = open("reg.txt", "r")
if reg_status_get:
    u_d = open("user_data1.csv", "r")
    reg_status = True
else:
    u_d = open("user_data1.csv", "w")

# vars
subject_user = ""
theme = 0
question = 0
all_questions = 0
percent_correct = 0
correct_answers = 0
incorrect_answers = 0
name_user = ""
class_user = 0
setter_name = ""
setter_subject = ""
setter_class = 0
formule_for_get_and_set = ["name", "subject", "class"]
questions_maths_7_function = {"""
Как читают запись y=f(x)?""":"функция f от переменной x, значение функции равно y",
"""Найдите значение функции y = 5x - 2x^2, соответствующее значению аргумента -1""":-7,
"""Найдите значение функции y = 6x + 19, если x = 0,5.""":22}

#functions

while True:
    def login_and_register():
        print("Вход в систему, подождите...")
        time.sleep(5)
        if reg_status:
            data_user = csv.reader(u_d)
            data_user_list = []
            for data in data_user:
                data_user_list.append(data)
            for i in range(0, 3):
                if formule_for_get_and_set[i] in data_user_list:
                    data_user_list.remove(formule_for_get_and_set[i])
            global name_user, subject_user, class_user
            name_user = data_user_list[0]
            subject_user = data_user_list[1]
            class_user = data_user_list[2]
            print("Вход выполнен. Здраствуйте,", name_user, "!")
        else:
            print("Аккаунт не найден. Создание нового")
            data_user_setting = csv.writer(u_d)
            data_user_setting.writerow(formule_for_get_and_set)
            user_set_data_list = []
            setter_name = input("Представьтесь системе: ")
            setter_class = int(input("Введите ваш класс (от 1 до 11): "))
            setter_subject = input("""
Выберите предмет (чтобы его выбрать, напишите английское название, которое находится рядом с вашим выбранным предметом):
Математика (Алгебра с 7 класса) - maths
---> """)
            user_set_data_list.append(setter_name)
            user_set_data_list.append(setter_subject)
            user_set_data_list.append(setter_class)
            data_user_setting.writerow(user_set_data_list)
            print("Аккаунт создан! Вход в него")

            print("Вход в систему, подождите...")
            time.sleep(5)
            data_user = csv.reader(u_d)
            data_user_list = []
            for data in data_user:
                data_user_list.append(data)
            for i in range(0, 3):
                if formule_for_get_and_set[i] in data_user_list:
                    data_user_list.remove(formule_for_get_and_set[i])
            global name_user, subject_user, class_user
            name_user = data_user_list[0]
            subject_user = data_user_list[1]
            class_user = data_user_list[2]
            print("Вход выполнен. Здраствуйте,", name_user, "!")