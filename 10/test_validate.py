email = "sinchan123v@gmail.com"

def main(mail):
    if check_dot_at(mail):
        print("Valid Email")
    else:
        print("Invalid Email")

def get_index(mail):
    count =0
    for char in mail:
        count+=1
        if char == '@':
            return count-1
        
def check_dot_at(mail):
    count =0
    mail_list = list(mail)

    for i in range(get_index(mail), len(mail_list)-1):
        if mail_list[i] == '.':
            count +=1
        else:
            pass
    if count == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    main(email)
    print(get_index(email))
    print(check_dot_at(email))
