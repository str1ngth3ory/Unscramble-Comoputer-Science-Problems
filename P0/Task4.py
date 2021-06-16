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

#Declare a checked list to store checked numbers
checked_numbers = []

#Declare a list to store telemarketer numbers
telemarketers = []

for call in calls:
    #Check if this number has been checked already. If yes, skip; if not, check it.
    if call[0] in checked_numbers:
        continue
    else:
        checked_numbers.append(call[0])
        telemarketers.append(call[0])
        #Check if this number ever received calls
        for call_2 in calls:
            if call_2[1] == call[0]:
                telemarketers.pop()
                break

        #Check if this number sent or received text if it passed the received call test
        if call[0] in telemarketers:
            for text in texts:
                if text[0] == call[0] or text[1] == call[0]:
                    telemarketers.pop()
                    break


#Sort the telemarketers list in lexicographic order
telemarketers.sort(key=str)

print('These numbers could be telemarketers:')
for number in telemarketers:
    print(number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
