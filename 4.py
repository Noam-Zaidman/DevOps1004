isTrue = False
a = 2
b = 2
strOne = "one"
strThree = "Three"
c = [1, 2, 3]
d = [1, 2, 3]
if type(a) is int:
    print(type(a))
if a == b:
    print("a equals to b")
if c == d:
    print("c equals to d")
if a is b:
    print("a is b")
if c is d:
    print("c is d")
age = int(input("enter you age: "))
if 0 < age < 120:
    print("ok")
my_names = ["adi", "ben", "noam", "arthur", "ron"]
if "zohar" in my_names:
    print("found it")

my_list = []

if my_list:
    print("my list is not empty")
if my_names:
    print("my_names is not empty")
if len(my_names) > 2:
    print("i rember enough names")
if a < b and not strThree == 3 or isTrue == 4:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
elif strOne != strThree:
    print("hello")
else:
    print("a is greater than b")

