import time

file = open('stopWords.txt', 'r')
stopWords = file.readlines() 

yesValidations = ['yes', 'Yes', 'yeah','Yeah', 'Thats fine']
noValidations = ['no', 'No', 'nah', 'Nah', 'No thanks']


response = raw_input ("What is your name? ")
time.sleep(1)

print("Hello " + response)
time.sleep(1)
response = raw_input ("I'd like to get to know a little about you, is that okay? ")
responseWords = response.split()
for word in responseWords:
    if word in yesValidations:
        time.sleep(1)
        print("That's Great, on to my first question")
    elif word in noValidations:
        time.sleep(1)
        print("If thats the case no need to continue, Good bye")

time.sleep(1)
response = raw_input ("What is your favorite colour? ")
time.sleep(1)
print(response +", mine is Purple" )

response = raw_input ("What is your favorite animal? ")
time.sleep(1)
print(response +", my favorite is Monkey" )


for response in stopWords:
    if response.replace(answer" ")
        
            stop_words = set(stop_words)
    for response in stopWords.intersection(raw_input):
        while response in raw_input:
            raw_input.remove(sw)

    return user_input