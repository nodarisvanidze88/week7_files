import csv

def get_data():
    with open("data.csv", "r") as file:
        infos = csv.DictReader(file)
        return [user for user in infos]


def add_new_data(data):
    fieldnames = ["First Name", "Last Name", "E-Mail", "Password", "LogIn Status"]
    with open("data.csv", "a", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow(data)

def write_new_data(data):
    fieldnames = ["First Name","Last Name","E-Mail","Password","LogIn Status"]
    with open("data.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)