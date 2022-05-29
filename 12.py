try:
    a = int(input("enter a number: "))
    b = int(input("enter second number: "))
    print(a / b)
    r = open("file_not_exisits.txt")
except ZeroDivisionError:
    print("could not divide by zero")
except FileNotFoundError:
    print("could not find file")
except Exception as e:
    print(e.args)
print("yes")



# import requests
# requests.get("ht5p://www.google.com")
