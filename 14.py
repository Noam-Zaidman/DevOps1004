from datetime import datetime


def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called.")
        func()
        print("something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("whee!")


say_whee()
