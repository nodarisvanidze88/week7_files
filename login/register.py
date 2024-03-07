import string
from utilities import get_data, add_new_data

def register():
    data  = collect_user_data()
    print(registration_method(data))

def registration_method(data):
    registation_status = check_user(data)
    if registation_status:
        add_new_data(data)
        return "Registration was successfuly"
    else:
        return f'User {data["E-Mail"]} is already in database'

def check_user(data):
    file_data = get_data()
    for item in file_data:
        if item["E-Mail"] == data["E-Mail"]:
            return False
    return True

def collect_user_data():
    first_name = first_last_name_validator("First Nmae: ")
    last_name = first_last_name_validator("Last Nmae: ")
    e_mail = e_mail_validation("E-Mail: ")
    password = pass_validator("Password: ", "Re_Password: ")
    status = "Inactive" 
    return {
        "First Name":first_name,
        "Last Name": last_name,
        "E-Mail" : e_mail,
        "Password": password,
        "LogIn Status": status
         }

def first_last_name_validator(txt):
    while True:
        user = input(txt)
        if user.isalpha():
            return user
        else:
            print("Wrong input")


def e_mail_validation(txt):
    while True:
        user = input(txt)
        if "@" in user and "." in user:
            return user
        else:
            print("Wrong e-mail format")

def pass_validator(txt, txt2):
    while True:
        user = input(txt)
        if any(i in string.ascii_letters for i in user) and any(i in string.punctuation for i in user) and any(i in string.digits for i in user) and len(user)>8:
            re_user = input(txt2)
            if user == re_user:
                return user
            else:
                print("Password is not matched")
                continue
        else:
            print("Password should be more then 8 symbols, should contains digit, alpha and special symbols")