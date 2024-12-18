# import random
# print("Hello python")
# if 5 < 2:
#  print("Five is greater than two!")
# else :
#  print("not an greter than")
# x = 5
# y = "Hello, World!"
# print(x)
# print(y)

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3) 

# print(type(x))
# print(type(y))
# print(type(z))



# my_var = "dn,mbgf"
# fruits = ["apple", "banana", "cherry"]
# x, y, z, = fruits
# print(x)
# print(y)
# print(z)
# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# # x = 5
# print(type(x))

# j = 50
# x = 3+5j
# y = 5j
# z = -5j

# print(x)
# print((y))
# print((z))

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# #convert from int to float:
# a = float(x)

# #convert from float to int:
# b = int(y)

# #convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# print(random.randrange(1, 5000))

# x = float(1)
# y = float(2.8)   
# z = float("3")  
# w = int("4.2")

# print(x)
# print((y))
# print((z))
# print((w))


# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#   print(x)

# print(len("banana"))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# a = "Hello, World!"
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("H", "J"))
# print(a.split(","))

# a = "Hello"
# b = "World"
# c = a + "                 " + b
# print(c)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)


# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# mytuple = ("apple", "banana", "cherry")
# print(mytuple)

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# # print(thistuple)

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)

# print(thisset)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict["colors"][0])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.values()
# print(x)

# thisdict  = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = thisdict.items()
# print(x)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)
# for x in thisdict:
#   print(x)

# for x in thisdict:
#  print(thisdict[x])

# def my_function():
#   print("Hello from a function")

# my_function()
# # _+_+_++_+_+++_+_+_+_+_+_+_+__+_+ keywordargument_+_+__+_+_+_+__+_+_+_+_+_+_+
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def myfunction():
#   pass

# def my_function(x, /):
#   print(x)

# my_function(3)

# def my_function(x):
#   print(x)

# my_function(x = 3)

# x = lambda a : a + 10
# print(x(5))
# class MyClass:
#   x = 5
# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()


# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()


# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

# x = Student("Mike", "Olsen", 2019)
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         print("Hello from B")

# class C(A):
#     def greet(self):
#         print("Hello from C")

# class D(B, C,A):  # Inherits from both B and C
#     pass
# print(D.__mro__)
# d = D()
# d.greet()
#   # Output depends on the MRO
# import platform

# x = platform.system()
# print(x)
# x = dir(platform)
# print(x)

# import datetime

# x = datetime.datetime.now()
# print(x)

# print(x.year)
# print(x.strftime("%A"))

# x = datetime.datetime(2020, 5, 17)

# print(x)

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.25)

# print(x)

# x = pow(4, 3)

# print(x)

# import math

# x = math.sqrt(64)

# print(x)


# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x) # returns 2
# print(y) # returns 1

# x = math.pi

# print(x)

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }


# y = json.loads(x)

# print(y)

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))

# json.dumps(x, indent=4)


# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())

# txt = "The rain in Spain"
# x = re.search("Portugal", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)


# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x) #this will print an object

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())

# import camelcase

# c = camelcase.CamelCase()

# txt = "hello world"

# print(c.hump(txt))

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# username = input("Enter username:")
# print("Username is: " + username)
# f = open("demofile.txt")
# f = open("demo.txt", "r")
# print(f.readline())
# f.close()
# f = open("demo.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demo.txt", "r")
# print(f.read())

# import os
# os.remove("demofile.txt")

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np


# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, 'o:r')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x1, y1, x2, y2)
# plt.grid()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# plt.scatter(x, y, c=colors)
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes,alpha=0.3)

# plt.show()

# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()

# x = np.random.normal(170, 10, 250)

# plt.hist(x)
# plt.show() 

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]

# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show() 

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# arr = np.array((1, 2, 3, 4, 5))
# arr = np.array(42)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)


# print(arr)

# print(np.__version__)


# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('Last element from 2nd dim: ', arr[1, -1])
# from scipy import stats

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = stats.mode(speed)


# import numpy
# speed = [86,87,88,86,87,85,86]

# x = numpy.std(speed)

# print(x)

# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.uniform(0.0, 5.0, 100000)

# plt.hist(x, 100)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy
# from scipy import stats
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# slope, intercept, r, p, std_err = stats.linregress(x, y)
# def myfunc(x):
#   return slope * x + intercept

# mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()

# import pandas
# from sklearn import linear_model

# df = pandas.read_csv("data.csv")
# X = df[['Weight', 'Volume']]
# y = df['CO2']
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
# predictedCO2 = regr.predict([[2300, 1300]])

# import numpy
# import matplotlib.pyplot as plt
# numpy.random.seed(2)

# x = numpy.random.normal(3, 1, 100)
# y = numpy.random.normal(150, 40, 100) / x
# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

# myline = numpy.linspace(0, 6, 100)

# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show()