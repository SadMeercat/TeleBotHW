from GroupHW_Python_ContactBook import change
# import import_contacts as imp
# import export as exp

filename = "GroupHW_Python_ContactBook\phones.txt"

def show_contacts():
    result = ""
    with open(filename, 'r', encoding="utf-8") as data:
        all_data = data.readlines()
    for item in all_data:
        result += item
    return result

def change_book(command, inpt_str: str):
    if command == 'd':
        if(inpt_str.isdigit()):
            return change.delete_contact(inpt_str)
        else:
            return "Неправильный ввод! Ожидается id контакта"
    elif command == 'a':
        return change.add_contact(inpt_str.split("\n"))
    elif command == 'u':
        tmp_list = inpt_str.split("\n")
        return change.change_contact(tmp_list[0],tmp_list)
        



#debug
print(show_contacts())