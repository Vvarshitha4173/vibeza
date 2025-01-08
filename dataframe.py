import pandas as pd
screen_time =[2,4,6]
sleep_hours = [3,7,8]
stu_name =["karthik","vivek","raju"]
dict1 = {
    "screen_time":screen_time,
     "sleep_hours":sleep_hours,
     "stu_name":stu_name
    }
print(dict1)
df = pd.DataFrame(dict1)
print(df)

import pandas as pd
name =["a","b","c"]
id = [1,2,3]
phone = [123,124,145]
dict1={
    "Name":name,
    "id": id,
    "phone_number":phone
    }
print(dict1)
df = pd.DataFrame(dict1)
print(df)

list = [2,1,13,15]
res = [i+2 for i in list if  i < 4]
print(res)
res = [i for i in list if i % 2 == 0]
print(res)

words = ["LOWER", "W", "PYTHON"]
lower= [i.lower() for i in words ]
print(lower)

# Output: ['HELLO', 'WORLD', 'PYTHON']

#Identifying Palindromes in a List of Words python
words = ["madam","radar","abc"]
result = [i for i in words if i == i[::-1]]
print("palindrome strings are ",result)

# conditionally modify the  elements
numbers = [-5, 3, -2, 8, -1]
resu = [x  if x>0  else 0  for  x in numbers]
print(resu)






non_negative = [x if x > 0 else 0 for x in numbers]
print(non_negative)
# Output: [0, 3, 0, 8, 0]

#Creating a Dictionary  comprehension From Two Lists
keys = ["name", "age", "city"]
values = ["banglore", 25, "Hyderabad"]
dictionary = {k:v for k,v in zip(keys,values)}
print(dictionary)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

#Finding Common Elements Between Two Lists
list =[1,2,3,4,5]
list1 =[3,5,8,9,1]
result = [i for i in list  if i in list1]
print(result)

#Finding List of squares
result = [x**2 for x in range(1,20)]
print(result)

# Squares of a number using dictionary comprehension
dict1 ={"a":12,"abc":123,"dfe":45}
result = {key:value for key,value in dict1.items()}
print(result)

# Range Practice #1
# Create a list consisting of all the numbers from 2500 to 2585 (inclusive). Store this list in the variable my_list.



# Range Practice #2
# Using the range() function, create in a single line of code a list consisting of all numbers that are multiples of 3 from 3 to 300 (inclusive). Store this list in the variable my_list.



# Range Practice #3
# Use the range() function and a loop to add the squares of all the numbers from 1 to 15 (inclusive). Store the result in a variable called sum_squares.

# Student Data Analysis
students = {"abc": 85, "def": 65, "ccc": 95, "chaina": 70}
passing_students = [name for name, score in students.items() if score >= 75]
grades = {name: "A" if score >= 90 else "B" for name, score in students.items()}
print(passing_students)
print(grades)

#organizing E commerce data
products = [
    {"name": "Laptop", "price": 800},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300}
]
affordable_products = {product["name"]: product["price"] for product in products if product["price"] <= 500}
print(affordable_products)
# Output: {'Smartphone': 500, 'Tablet': 300}





products = [
    {"name": "Laptop", "price": 800},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300}
]
affordable_products = {product["name"]: product["price"] for product in products if product["price"] <= 500}
print(affordable_products)
# Output: {'Smartphone': 500, 'Tablet': 300}

import math
list =[4,6,36]
result = tuple(math.sqrt(i) for i in list)
print(result)

import math
numbers = [1, 4, 9, 16, 25]
square_roots = tuple(math.sqrt(num) for num in numbers)
print(square_roots)

#Functions
#Lamda functions
#c. Nested Functions
#Decarators

square = lambda x:x**2 in range(1,10)
print(square)

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 5, "add"))  # Output: 15

