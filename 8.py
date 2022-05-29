def validate(prompt, low, high, ok, not_ok):
    input_from_user = int(input(prompt))
    if low < input_from_user < high:
        return ok
    else:
        return not_ok


print(validate("enter your age: ", 0, 120, "age is good", "age is not ok"))
