# Task 1

sent_1=input("Please,enter: ")
dict_1={}
for word in sent_1.split():
    if word in dict_1:
        dict_1[word]+=1
    else:
        dict_1[word]=1
print(dict_1)

 #or

input_sent=input("Please,enter: ").split()
print({i:input_sent.count(i) for i in input_sent})

# Task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total = 0

for stock1 in stock.keys():
  for price in prices.keys():
    if stock1 == price:
      total += stock.get(stock1) * prices.get(price)
print(total)


# Task 3
list1=[(i,j) for i in range(1,11) for j in[i**2]]
print (list1)

# Task 4

val= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
keys= [1, 2, 3, 4, 5, 6, 7]
dictionary = dict(zip(keys, val))
e={v:k for k,v in dictionary.items()}
print(dictionary)
print(e)
