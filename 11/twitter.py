import re

url = input("whats url?")

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)

print(f"Username :{username}")