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

# program to gate last element of the list-----------------------------P57
