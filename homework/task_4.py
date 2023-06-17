
#Task1

string="beetroot academy"
if len(string)<2:
    print("")
else:
    print(string[0:2] + string[-2:])  

#Task2

number="1281734554"
if len(number)==10 and number.isdigit:
    print("Your number is good")
else:
    print("Change your number")

#Task3

answer=True
if answer:
    print("Your answer is true")
else:
    print("Your answer is false")

#or

vyraz=60/15
if vyraz==4:
    print("Your answer is true" )
else:
    print("Your answer is false")

#Task 4

my_name="maria"
input_name="MAria"

if my_name==input_name.lower():
    print(True)
else:
    print(False)

#or

my_name_1="diana"
input_name_1=input("Please,enter your name: ").lower()
print(my_name_1==input_name_1)




