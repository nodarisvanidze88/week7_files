from utilities import get_data
from register import register

def main():
    print("Welcom to our Test System, please select the answer")
    first_answer = first_question()
    if first_answer =="1":
        register()

    

def first_question():
    answers = ["1","2","3"]
    selection = {1: "Registration",
                 2: "Log In",
                 3: "Log Out"}
    while True:
        for i in selection.items():
            print(f"{i[0]}. {i[1]}")
        user = input("What action you want registration or login or logout? ")
        if user in answers:
            return user
        else:
            print("\nPlease select folowing number (e.g. 1,2 or 3)")
            continue



if __name__ =="__main__":
    main()