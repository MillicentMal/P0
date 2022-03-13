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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
incoming_calls = []
outgoing_calls = []
outgoing_texts = []
incoming_texts = []
for i in range(len(calls)):
    outgoing_calls.append(calls[i][0])
    incoming_calls.append(calls[i][1])
for i in range(len(texts)):
    outgoing_texts.append(texts[i][0])
    incoming_texts.append(texts[i][1])
    
all_numbers = incoming_calls + outgoing_calls + outgoing_texts + incoming_texts
different_numbers = set(all_numbers)

counter = len(different_numbers)
print("There are " + str(counter) + " different telephone numbers in the records.")