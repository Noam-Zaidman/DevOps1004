import requests

from datetime import  datetime
my_file = open("read my content.txt", "w")
my_file.write("hello from mars the date is: " + str(datetime.now()))
my_file.close()


def get_name():
    n = input("enter your name: ")
    my_file = open("names.txt" , "a")
    my_file.write(f"{n}\n")


def show_names():
    with open("names.txt") as my_file:
        for line in my_file.readlines():
            print(f" hello {line}", end = '')


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")


def call_urls():
    with open("urls.txt") as urls:
        for line in urls.readlines():
            url_caller(line.strip())



# save_name()
show_names()