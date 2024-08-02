# program to short a dictionary by value -------------------------------------P49
# ---------solution 1 ---------------
# marks = {"prince": 76, "prashant": 97, "priyanshu": 46}
# shorted_marks = sorted(marks.items(), key=lambda x: x[1])
# print(shorted_marks)
# ---------solution 2 sort only the value
# v = sorted(marks.values())
# print(v)

# to check if a list is empty----------------------------------------------P50
# solution 1
# my_lsit = []
# if not my_lsit:
#     print("the list is empty")
# solution 2 using len()
# if len(my_lsit) == 0:
#     print("the list is empty")
# solution 3 using square brackets
# if my_lsit == []:
#     print("the list is empty")


# program to catch multiple exeptions in one line --------------------------------P51
# string = input("enter something here:")
# try:
#     num = int(input("enter a number here:"))
#     print(string + num)
# except (ValueError, TypeError) as a:
#     print(a)


# how to copy content from one file to another ------------------------------------P52
# from shutil import copyfile
# copyfile("C:/Users/pc/Desktop/python/demo.txt",
#          "C:/Users/pc/Desktop/python/file.txt")

# program to concatenate two lists ------------------------------------------------P53
# solution 1 using + operator
# l1 = [4, 6, 2, 8, "t,u"]
# l2 = ["k", "t", 3, 7, 9, "v"]
# l12 = l1+l2
# print(l12)

# solution 2 using unique value
# l1 = [4, 6, 2, 8, "t,u"]
# l2 = ["k", "t", 3, 7, 9, "v"]
# l12 = set(l1+l2)
# print(l12)

# solution 3 using extend()
# l1 = [4, 6, 2, 8, "t,u"]
# l2 = ["k", "t", 3, 7, 9, "v"]
# l1.extend(l2)
# print(l1)

# program to check if a key is already in dictionary------------------------------P54
# frineds = {"prashant": "sharma", "priyanshu": "mathur", "rahul": "verma"}
# name = input("enter a key here:")
# if name in frineds.keys():
#     print("it is present")
# else:
#     print("it is not present")

# parse a string into float or int ------------------------------------------P55
# solution 1 parse string into integer / float
# string = "12345"
# int_str = int(string)
# float_str = float(string)
# print(int_str)
# print(float_str)

# solution 2 parse string float numeral into integer
# string = "123.45"
# str_float_int = int(float(string))
# print(str_float_int)


# program to convert string to datetime----------------------------------P56
# solution 1 using date time module
# from datetime import datetime
# date = "july 26 2000 4:05AM"
# date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
# print(date_time)
# print(type(date_time))

# solution 2 using dateutil module
# from dateutil import parser
# date_time = parser.parse("july 26 2000 4:05AM")
# print(date_time)
# print(type(date_time))

# program to get last element of the list-----------------------------P57
# name = ["sonu", "monu", "saurabh", "munna"]
# print(name[-1])

# program to get substrikng from a string------------------------------P58
# string = "hello my name is saurabh anand"
# print(string[16:24])

# print output without a newline -----------------------------------P59
# print("hello my name is :", end="")
# print("saurabh anand ")

# check if a string is a valud keyword or not-------------------------P60
# import keyword
# words = ["hello", "keywords", "break", "saurabh", "sachin", "string", "lambda"]
# for i in range(len(words)):
#     if keyword.iskeyword(words[i]):
#         print(words[i], "is a keywords in python")
#     else:
#         print(words[i], "is not a keywords in python")

# python iterators along with next function-------------------------------P61
# string = "sachin rao"
# for i in string:
#     print(i)
# iterate = iter(string)
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(next(iterate))

# solution 2 creating iter function
# class five:
#     def __init__(self):
#         self.num = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.num <= 5:
#             value = self.num
#             self.num += 1
#             return value
#         else:
#             raise StopIteration


# ff = five()
# for i in ff:
#     print(i)

# list comparison --------------------------------------P62
# avengers = ["ironman", "batman", "captainamerica", "thor", "groot", "antman"]
# new_avenger = [i.upper() for i in avengers]
# print(new_avenger)

# m = [i for i in range(10)]
# print(m)
# k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
# for i in k:
#     if i % 2 == 0:
#         new_list.append(i)
# print(new_list)
# m = [i for i in range(10) if i % 2 == 0]
# print(m)


# --------------------remove the comments except first line of every program and enjoy -----------------------
