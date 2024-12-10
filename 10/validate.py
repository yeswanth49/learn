email = input("whats email?").strip()

def main(mail):
    if single_at_check(mail) and first_at_dot(mail) and check_dot_at(mail):
        print("Valid Email")
    else:
        print("Invalid Email")

def single_at_check(mail):
    count =0
    for char in mail:
        if '@' ==char:
            count = count+1
    if count == 1:
        return True
    else :
        return False
    
def first_at_dot(mail):
    if '.' in mail and mail[0] != '@' and mail[0] != '.':
        return True
    else :
        return False

def get_index(mail):
    count =0
    for char in mail:
        count+=1
        if char == '@':
            return count
        
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
