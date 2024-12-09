import sys

try:
    for arg in sys.argv[1:]:
        print(arg)


except IndexError:
    print("You have to pass an argument")