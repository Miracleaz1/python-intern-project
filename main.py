# def print_hello(name:str) -> str:
#     return f"Hello, {name}!"
# response = print_hello("Miracle")
# print(response)

# user = {"name": "Miracle", "age": "15", "department": "IT"}

# #print(user["department"])

# a = 5
# b = 13

# print(a + b)
# print(a - b)
# print(a * b)
# #modulus
# print(a%b) #this result in reminder value
# print(a/b)

# #string
# my_string = "Hello world"
# print(my_string)

# my_real_string = '''Hello

# we are to create string on multiples line using this type of quote
# world
# '''
# print(my_real_string)

# #slicing in python
# name = "Miracle Azenabor"
# #slice = name[0]
# #slice = name[1:10]
# #slice = name[:10]
# #slice = name[-10:]
# #the syntax of string slicing is
# #string[start:end:step]
# #slice = name[-10:]
# slice = name[1:5:2]
# print(slice)

# #strig cases
# name = " Miracle Azenabor "
# name_upper = name.upper()
# print(name_upper)
# name_lower = name.lower()
# #print(name_lower)
# #print(name.strip())
# new_name = name.strip().replace("Azenabor", "Osemudiamen")
# print(new_name)
# name_list = name.strip().split()
# print(name_list[1])

# #string formating
# name = "Miracle Azenabor"
# greetings = "Good Morning!"
# #message = "{} Say's {}".format(name, greetings)
# #message = "{name} Say's {greetings}".format(name=name, greetings=greetings) #adding the f'string
# message = "%s say's %s" % (name,greetings)
# print(message)

# #boolean in python
# #a = 5
# #b = 10
# #print(a == b)
# #print(a < b)
# #using logical operation
# a = True #1
# b = False #0
# print(a and b)
# print(a or b)
# print(not a)

# #truthiness in python
# #truthy and falsy
# #falsy
# none = "", (), {}, []

# #truthy
# num1 = 1# this is truth
# num1 = 0 # this is falsy
# num1 = ()# this is falsy

# #Constant in python
# PI = 3.142

# #type convertion in python
# x: int = 20
# y: str = str(x)
# print(type(x))
# print(type(y))

# conditional statement
# if statment in python
# first_name = "Miracle"
# if first_name == "Wisdom":
#     print(" Bravo yeah that is my name!")
# else:
#     print("you don't know my name you don f**k up")

# # for loop in python
# fruit_list = ("apple", "banana", "Mango", "Orange")
# for fruit in fruit_list:
#     print(fruit)

# for i in range(20):
#     if i == 0:
#         continue
#     elif i == 24:
#         break
#     print(i)
#     if i % 2 == 0:
#         sample = f"{i} - even number"
#         print(sample)
#     else:
#         sample = f"{i} - odd number"
#         print(sample)
        
    # Example of a while loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1
    
# max = 50
# count = 2
# while count < max:
#         print(f" we are live {max}")
# count += 2

# function in python
def print_hello(greetings, friends_name) -> str:
    """
    This function takes that
    say hello to our friends
    """
    # this is where you write your code
    return f"Hello, {friends_name}! Good {greetings}!"
# this is where you call your function
response = print_hello("Morning", "Miracle")
print(response)