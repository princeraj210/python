# fibonacci sequence using recursion----------------------P32
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)


# n = int(input("enter the umber of sequence:"))
# if n <= 0:
#     print("please enter the positive number")
# else:
#     print("fbonacci sequence :")
#     for i in range(n):
#         print(fibo(i))

# sum of natural number using recursion ---------------------P33
# def natural(n):
#     if n <= 0:
#         return n
#     else:
#         return (n)+natural(n-1)


# n = int(input("enter the number:"))
# if n <= 0:
#     print("please enter positive number.")
# else:
#     print("the sum of natural number is :", natural(n))


# find factorial of number using recursion -------------------P34
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return (n*fact(n-1))


# n = int(input("enter the number:"))
# if n <= 0:
#     print("factorial of number less thaan 1 is not exixt.")
# else:
#     print("the factorial of given number is :", fact(n))


# convert binary to decial using recursion------------------P35
# def ConvertBinary(n):
#     if n > 1:
#         ConvertBinary(n//2)
#     print(n % 2, end="")


# print("the binary of given number is :")
# ConvertBinary(22)

# program to add two matrices-----------------------P36
# A = [[1, 5, 8],
#      [4, 6, 7],
#      [7, 2, 3]]
# B = [[4, 5, 6],
#      [8, 9, 1],
#      [3, 5, 6]]
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result[i][j] = A[i][j]+B[i][j]
# for r in result:
#     print(r)

# program to transpose of matrics -----------------P37
# A = [[1, 2, 3],
#      [4, 5, 6]]
# result = [[0, 0],
#           [0, 0],
#           [0, 0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result[j][i] = A[i][j]
# for k in result:
#     print(k)


# check wheather a string is pelindrome or not -----------------P38
# word = input("enter a word here:")
# rev = word[::-1]  # it reverse the string
# if word == rev:
#     print("it is a pelindrome word.")
# else:
#     print("it is not pelindrome word.")


# remove punctuation from string ---------------------------P39
# punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# string = input("enter your sentance:")
# empty_string = ""
# for i in string:
#     if i not in punc:
#         empty_string += i
# print(empty_string)


# program to multiply two matrices-----------------------P40
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = [[1, 2, 1, 1],
#      [4, 2, 1, 2],
#      [6, 3, 4, 1]]
# result = [[0, 0, 0, 0],
#           [0, 0, 0, 0],
#           [0, 0, 0, 0]]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j] += A[i][k]*B[k][j]
# for i in result:
#     print(i)

# program to sort word in alphabetical number----------------P41
# a = input("enter sentances here:")
# w = a.split()
# for i in range(len(w)):
#     w[i] = w[i].lower()
# w.sort()
# for i in w:
#     print(i)

# python program to set different operations -------------------P42
# A = {1, 2, 3, 6, 8, 9}
# B = {3, 4, 5, 6, 7, 8}
# print("the union is :", A | B)
# print("the intersection is :", A & B)
# print("the difference is :", A-B)
# print("the symmetric diffrence is :", A ^ B)

# program to count the number of each vowels---------------------P43 PART 1
# ~~~~~~~~~~~using dictionary~~~~~~~~~~~~~~~~~~
# a = "hii my Name is PRince chaubey"
# vowels = "aeiou"
# a = a.casefold()
# count = {}.fromkeys(vowels, 0)
# for char in a:
#     if char in count:
#         count[char] += 1
# print(count)

# program to count the number of each vowels---------------------P43 PART 2
# ~~~~~~~~~~~~~using list and dictionary comprehension~~~~~~~~~~~~~~
# a = "Hii My name IS prince Chaubey"
# vowels = "aeiou"
# a = a.casefold()
# count = {key: sum([1 for char in a if char == key])for key in vowels}
# print(count)

# program to find size(resolution ) of an image ----------------------P44
# import PIL
# from PIL import Image
# img = PIL.image.open(
#     "C:/Users/pc/Desktop/professional profile/Prince Portfolio/Png Image/IMG_20230412_211424")
# width , height = img.size
# print(width , "x" , height)

# Program to merge two dictionary -----------------------------P45
# solution 1 using | operator
# dict1 = {"john": 89, "lisa": 99}
# dict2 = {"lisa": 94, "peter": 78}
# print(dict1 | dict2)

# aolution 2 using **operator
# dict1 = {"john": 89, "lisa": 99}
# dict2 = {"lisa": 94, "peter": 78}
# print({**dict1, **dict2})

# solution 3 using copy() and update() method
# dict1 = {"john": 89, "lisa": 99}
# dict2 = {"lisa": 94, "peter": 78}
# dict3 = dict2.copy()
# dict3.update(dict1)
# print(dict3)

# program to access index of a list using for loop-----------------P46
# solution 1 using enumerate method
# list1 = [23, 5, 67, 98, 32]
# for index, value in enumerate(list1, start=1):
#     print(index, "-", value)

# solution 2 not using enumerate function
# list1 = [23, 5, 67, 98, 32]
# for i in range(len(list1)):
#     value = list1[i]
#     print(i, value)


# Program to slice a list -----------------------------P47
# a = ["prince", "piyush", "adarsh", "shivam"]
# slice = a[1:2]
# print(slice)

# program to itterate over dictionaries using for loop ----------------------P48
# human = {"john": "male", "cristina": "female", "joe": "shemale"}
# print(human)
# solution 1 with .items

# for key, value in human.items():
#     print(key, ":" , value)
# SOLUTION 2 WITH KEYS
# for key in human:
#     print(key, human[key])

# solution 3 with key and values
# for key in human.keys():
#     print(key)
# for i in human.values():
#     print(i)


# --------------------remove the comments except first line of every program and enjoy -----------------------
