'''2.Provide a program to read the CSV file.
• CSV file has three columns, the first column names, the second column is birthdate(YYYYMM-DD) the third column is salary.
• Read the file and display the data and age in the terminal.
• The file path, delimiter, and quote char are the input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal.
'''

import csv
from datetime import date
from datetime import datetime

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return str(age)

path = input()

with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row, age(datetime.strptime(row[1], '%Y-%m-%d')))
