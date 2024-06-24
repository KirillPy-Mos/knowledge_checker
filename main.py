# imports
import random, time, csv

# connect to files
reg_status_set = open("reg.txt", "w")
reg_status_get = open("reg.txt", "r")
if reg_status_get:
    u_d = open("user_data1.csv", "r")
else:
    u_d = open("user_data1.csv", "w")

# vars
subject = ""
theme = 0
question = 0
all_questions = 0
percent_correct = 0
correct_answers = 0
incorrect_answers = 0
name = ""
mode = ""
setter_name = ""
setter_subject = ""
setter_mode = ""
