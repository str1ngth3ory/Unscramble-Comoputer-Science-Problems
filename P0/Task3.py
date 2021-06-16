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

#Declare empty list to store unique codes or prefixes
codes_by_ba = []

#Declare counter for Bangolore to Bangolore calls
count = 0

#Extract area codes or prefixes of receiving numbers from calls made by person from Bangalore
for call in calls:
    if call[0].startswith('(080)'):
        if '(' in call[1]:
            code = call[1][:call[1].find(')')+1]
        elif call[1].startswith('1'):
            code = '140'
        else:
            code = call[1][:4]

        #check for duplicates
        if code not in codes_by_ba:
            codes_by_ba.append(code)

        #check if the receiver is also a fixed line from Bangolore
        if call[1].startswith('(080)'):
            count += 1

#Sort in lexicographic order
codes_by_ba.sort(key=str)

print('The numbers called by people in Bangalore have codes:')
for code in codes_by_ba:
    print(code)

#Calculate the percentage for Part B
per_bang_to_bang = count / len(calls)
print('{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(per_bang_to_bang))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
