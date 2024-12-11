import re

name = input("whats name?").strip()
matches = re.search(r"^(.+), ?(.+)$",name)
if matches:
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"hello, {name}")