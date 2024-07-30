# program to short a dictionary by value -------------------------------------P49
# ---------solution 1 ---------------
marks = {"prince": 76, "prashant": 97, "priyanshu": 46}
shorted_marks = sorted(marks.items(), key=lambda x: x[1])
print(shorted_marks)
# ---------solution 2 sort only the value
v = sorted(marks.values())
print(v)

# to check if a list is empty----------------------------------------------P50
# solution 1
my_lsit = []
if not my_lsit:
    print("the list is empty")
# solution 2 using len()
if len(my_lsit) == 0:
    print("the list is empty")
# solution 3 using square brackets
if my_lsit == []:
    print("the list is empty")


# program to catch multiple exeptions in one line --------------------------------P51
string = input("enter something here:")
try:
    num = int(input("enter a number here:"))
    print(string + num)
except (ValueError, TypeError) as a:
    print(a)
