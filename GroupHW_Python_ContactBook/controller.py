
filename = "GroupHW_Python_ContactBook\phones.txt"

def show_contacts():
    result = ""
    with open(filename, 'r', encoding="utf-8") as data:
        all_data = data.readlines()
    for item in all_data:
        result += item
    return result

def change_book(command, inpt_str):
    if command == 'd':
        return
    elif command == 'a':
        return

#debug
print(show_contacts())