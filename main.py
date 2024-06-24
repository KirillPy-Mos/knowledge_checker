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
formule_for_set = "name,subject,class"
formule_for_get = ["name", "subject", "class"]

#functions

while True:
    def login():
        print("Вход в систему, подождите...")
        if reg_status:
            data_user = csv.reader(u_d)
            data_user_list = []
            for data in data_user:
                data_user_list.append(data)
            for i in range(0, 3):
                if formule_for_get[i] in data_user_list:
                    data_user_list.remove(formule_for_get[i])
            global name_user, subject_user, class_user
            name_user = data_user_list[0]
            subject_user = data_user_list[1]
            class_user = data_user_list[2]
            print("Вход выполнен. Здраствуйте,", name_user, "!")


