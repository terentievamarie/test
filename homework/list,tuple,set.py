
# Task 1

import random
random_list=[]
i=0
while i<10:
    random_list.append(random.randint(1,100))
    i+=1
maxi=random_list[0]
j=0
while j<10:
    if (random_list[j]>maxi):
        maxi=random_list[j]
    j+=1
print(random_list)
print(maxi)


#or 

from functools import reduce
from random import randint
list1=[randint(-10,25) for i in range(30)]

print(list1)
print(reduce(max,list1))

# Task 2


from random import randint
list_1=[randint(1,10) for i in range(10)]
list_2=[randint(1,10) for i in range(10)]
list_3=list_1 + list_2
print(list_1)
print(list_2)
print(set(list_3))

#or
import random
first_list=[]
second_list=[]
i=0
j=0
while i<10:
    first_list.append(random.randint(1,10))
    i+=1
while j<10:
    second_list.append(random.randint(1,10))
    j+=1
third_list=[]
h=0
while h<10:
    third_list.append(first_list[h])
    h+=1
k=0
while k<10:
    third_list.append(second_list[k])
    k+=1
fourth_list=set(third_list)
print(fourth_list)

# Task 3
import random
new_list=[i for i in range(1, 101)]
new_list_2=[i for i in new_list if i%7==0 and i%5!=0]
print (new_list)
print(new_list_2)
