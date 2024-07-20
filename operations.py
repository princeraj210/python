# sqrt manually --------
# num = int(input("etner the number:"))
# sqrt = num**(1/2)
# print(sqrt)

# find sqrt with math module-------
# import math
# num = int(input("etner the number:"))
# sqrt = math.sqrt(num)
# print(sqrt)

# area of triangle --------
# base = int(input("enter base :"))
# height = int(input("enter height:"))
# area = (1/2) * base * height
# print(area)

# swapping of two veriable ---------
# x = 12
# y = 13
# temp = x
# x = y
# y = temp
# print("x =", x)
# print("y =", y)

# swapping of two number left right--------
# x = 97
# y = 34
# x, y = y, x
# print("x=", x)
# print("y=", y)
# kilometer to miles converter --------
# kilo = float(input("enter in KM= "))
# miles = 0.621371*kilo
# print(miles)

# check number is positive negative or zero ------
# num = int(input("enter the number:"))
# if num == 0:
#     print("number is zero")
# elif num > 0:
#     print("number is positive")
# else:
#     print("number is negative")

# check number is even of odd-----------------
# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# program to check leap year-------------------
# year = int(input("enter the year:"))
# if (year % 4 == 0 and year % 400 == 0):
#     print("entered year is leap year.")
#     if (year % 400 == 0 and year % 100 != 0):
#         print("entered year is leap year")
# else:
#     print("entered year is not a leap year")

# largest among three number --------------------
# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))
# num3 = int(input("enter the third number :"))
# if num1 > num2 and num1 > num3:
#     print(num1, "is greater.")
# elif num2 > num1 and num2 > num3:
#     print(num2, "is greater.")
# else:
#     print(num3, "is greater.")

# check number is prime ------------------
# num = int(input("enter the number:"))
# if num > 1:
#     for i in range(2, num-1):
#         if num % i == 0:
#             print("it is not a prime number")
#             break
#         else:
#             print("it is a prime number")
#             break
# else:
#     print("enter the positive number")

# program to generate random number-----------------
# import random
# num = random.randint(1, 100)
# print(num)

# print every prime number between given value------------
# lower1 = int(input("enter the lower value:"))
# upper = int(input("enter the upper value:"))
# for num in range(lower1, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# convert celcius into fahrenheit---------------
# celcius = int(input("enter tempreture in celcius:"))
# fahrenheit = (celcius*(1.8))+32
# print("fahrenheit is ", fahrenheit)

# factorial of a number ---------------
# num = int(input("enter a number:"))
# fact = 1
# if num > 0:
#     for i in range(1, num+1):
#         fact  *= i
# print("factorial of ", num, "is ", fact)

# factorial by recursion ----------------------
# def fact(a):
#     if a == 0:
#         return 1
#     else:
#         return (a * fact(a-1))


# num = int(input("enter the number:"))
# result = fact(num)
# print("factorial of given number is ", result)

# print multiplication table ---------------
# num = int(input("enter the number:"))
# for i in range(1, 10):
#     print(num, "x", i, "=", num*i)

# multiplication table by while loop ------------
# num = int(input("enter the number:"))
# i = 1
# while (i <= 10):
#     print(num, "x", i, "=", num*i)
#     i += 1

