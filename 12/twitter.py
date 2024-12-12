import re

url = input("whats url?").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)/?",url,re.IGNORECASE) :
    username = matches.group(1)
    print(f"Username is {username}")