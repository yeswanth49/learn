def main():
    x = get_int("value of x")
    print(f"x is {x}")

def get_int(prompt = "what's x?"):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()