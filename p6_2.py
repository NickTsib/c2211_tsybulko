try:
    print("start code")
    print(10/0)
    print("No errors")
except NameError:
    print("We have NameError")
except ZeroDivisionError:
    print("We have ZeroDivisionError")

print("code after capsule")