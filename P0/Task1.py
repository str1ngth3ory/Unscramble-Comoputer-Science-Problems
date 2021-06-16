"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

phone_nums = []
for text in texts:
    phone_nums += text[0], text[1]
for call in calls:
    phone_nums += call[0], call[1]

number_of_unique_nums = len(set(phone_nums))
print('There are {} different telephone numbers in the records.'.format(number_of_unique_nums))


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
