#Task 1

name="Mary"
day="Monday"
print(f"Good day {name}! {day} is a perfect day to learn some python.")
print("Good day"+ " " +name +"!"+ " " + day +" " + "is a perfect day to learn some python.")
print("Good day {}! {} is a perfect day to learn some python.".format(name,day))

#Task 2

my_name="Maria"
my_surname="Terentieva"
my_in=my_name +" " + my_surname 
print(my_in + ", Happy Birthday!")
print(f"{my_in}, Happy Birthday!")
print("{}, Happy Birthday!".format(my_in))

#Task 3

a=10
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b) #остача від ділення 10 на 7
print(a//b) # скільки разів націло ділиться 10 на 7