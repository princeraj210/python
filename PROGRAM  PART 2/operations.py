# find armstrong number in interval -----------------P21
# lower = int(input("enter the lower number:"))
# upper = int(input("enter the upper number:"))
# for i in range(lower, upper+1):
#     order = len(str(i))
#     sum = 0
#     temp = i
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#     if i == sum:
#         print(i)


# find the sum of natural number---------------P22
# num = int(input("enter natural number:"))
# sum = 0
# if num < 0:
#     print("please enter positive number")
# elif num == 0:
#     print("its a zero number")
# else:
#     for i in range(1, num+1):
#         sum += i
#     print("the sum of ", num, "is ", sum)


# Program to display power of two using lambda function--------P23
# num = int(input("enter the term you want :"))
# result = list(map(lambda x: 2**x, range(num+1)))
# print(result)


# find number divisible by another number -------------------P24 PART 1
# print("---------number is divisible by 12-----------")
# lower = int(input("enter the lower limit:"))
# upper = int(input("enter the upper limit:"))
# for i in range(lower, upper+1):
#     if i % 12 == 0:
#         print(i)

# find number divisible by another number by lambda / filter -------------------P24 PART 1
# list1 = {39, 26, 48, 98, 33, 67, 87}
# result = list(filter(lambda x: x % 13 == 0, list1))
# print(result)

# program to convert decimal to binary, octal and hexadecimal ------------------P25
# decimal = int(input("enter the number here:"))
# print("the conversion of decimal number ", decimal, "is")
# print(bin(decimal), "in binary")
# print(oct(decimal), "in octal")
# print(hex(decimal), "in hexadecimal")  # it also print the prefix of the number


# find ASCHII value of any character -----------------P26
# char = input("enter any character:")
# print("the ASCHII value of ", char, "is", ord(char))

# program to find HCF or GCD-------------------P27
# def findHCF(x, y):
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1, smaller+1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
# print("the HCF of given number is ", findHCF(12, 30))

# find the factor of a number---------------------P28
# num = int(input("enter the number :"))
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)


# program to make a simple calculator----------------P29
# print("~~~~~~~~mini calculator~~~~~~~~~~~~")
# num1 = float(input("enter the first operand:"))
# num2 = float(input("enter the second operand:"))
# print("press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division")
# choice = int(input("enter your choice: "))
# if choice == 1:
#     print("the addition of two number is ", (num1+num2))
# elif choice == 2:
#     print("the subtraction of two number is ", (num1-num2))
# elif choice == 3:
#     print("the Multiplication of two number is ", (num1*num2))
# elif choice == 4:
#     print("the division of two number is ", (num1/num2))
# else:
#     print("your choice is wrong")

# program to suffle deck of cards--------------------P30
# import random
# import itertools
# deck = list(itertools.product(range(1, 14), [
#             "spade", "club", "hearts", "diamond"]))
# random.shuffle(deck)
# for i in range(5):
#     print(deck[i][0], "of", deck[i][1])

# display calander month --------------------P31
# import calendar
# year = int(input("enter the year :"))
# month = int(input("enter the month :"))
# calender = calendar.month(year, month)
# print(calender)


# --------------------remove the comments except first line of every program and enjoy -----------------------
