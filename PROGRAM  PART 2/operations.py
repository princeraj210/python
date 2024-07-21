# find armstrong number in interval -----------------P21
lower = int(input("enter the lower number:"))
upper = int(input("enter the upper number:"))

for i in range(lower, upper+1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if i == sum:
        print(i)
