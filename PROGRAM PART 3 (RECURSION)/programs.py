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
word = input("enter a word here:")
rev = word[::-1]  # it reverse the string
if word == rev:
    print("it is a pelindrome word.")
else:
    print("it is not pelindrome word.")
