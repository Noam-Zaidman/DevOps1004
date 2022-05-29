import requests
try:
    requests.get("huiuh; jkljkl")
except requests.exceptions.HTTPError:
    print("missing schema in url")


# def get_age():
#     age = int(input("enter your age: "))
#     if age < 0:
#         raise ValueError("age can not be negative")
#
#
# a = int(input("enter a number: "))
# def check_my_number(num):
#     a = ""
#     try:
#         a = int(num)
#     except ValueError:
#         return False
#     if str(num).isdecimal() or str(num).isdigit()
# try:
#     get_age()
# except ValueError as e:
#     print(e.args)