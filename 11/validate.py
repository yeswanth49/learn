import re

email = input("whats email?")

if re.search('@',email):
    print("Valid")
else:
    print("Invalid")