#Task 1

import random
random_number=random.randint(1,10)
cus_number=int(input("Please,enter your number:"))
if random_number==cus_number:
    print("That's awesome!")
else:
    print("Try again!")
print(f"My number was:  {random_number}")


#Task 2

your_name=input("Please,enter your name: ")
your_age=int(input("Please,enter your age: "))

print(f"Hello {your_name}, on your next birthday you’ll be {your_age + 1} years")

#Task 3
import random
input_string=input("Please,enter your string: ")
input_list=list(input_string)
for words in range(5):
    random.shuffle(input_list) # changes the order of elements in the list
    print("".join(input_list)) # makes a string from list
