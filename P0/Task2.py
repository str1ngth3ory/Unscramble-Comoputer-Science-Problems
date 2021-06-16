"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#Declare a dictionary to store phone number vs call length in seconds
call_length_dict = {}

for call in calls:
    #Accumulate seconds for each caller number
    if call[0] not in call_length_dict:
        call_length_dict[call[0]] = int(call[3])
    else:
        call_length_dict[call[0]] += int(call[3])
    #Accumulate seconds for each receiver number
    if call[1] not in call_length_dict:
        call_length_dict[call[1]] = int(call[3])
    else:
        call_length_dict[call[1]] += int(call[3])

#Search for the phone number with the longest call time
longest_phone_num = max(call_length_dict, key=call_length_dict.get)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(longest_phone_num, call_length_dict[longest_phone_num]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
