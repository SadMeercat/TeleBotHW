#инициализация переменных 
def __init__():
    global file
    file = 'GroupHW_Python_ContactBook\phones.txt'

def add_contact(cont_data: list) -> str:
    try:
        with open(file, 'r', encoding='utf-8') as data:
            my_data = data.readlines()
        last_id = my_data[len(my_data) - 1].split(' ')[0]
        tmp_contact = f"{int(last_id) + 1} {cont_data[0]}\t{cont_data[1]}\t\
        {cont_data[2]}\t{cont_data[3]}\t{cont_data[4]}"
        with open(file,'a', encoding='utf-8') as data:
            data.write(tmp_contact)
        return "Контакт успешно добавлен"
    except:
        return "Что-то пошло не так... У программиста кривые руки"

def delete_contact(id) -> str:
    with open(file,'r',encoding='utf-8') as data:
        my_data = data.readlines()
    title = my_data[0]
    del my_data[0]
    del my_data[int(id)-1]

    counter = 1
    tmp_list = []
    for i in my_data:
        tmp_list.append(i.split(" "))
    print(tmp_list)
    my_data.clear()
    my_data.append(title)
    for i in tmp_list:
        i[0] = str(counter)
        my_data.append(f"{i[0]} {i[1]}")
        counter += 1
    
    with open(file,'w',encoding='utf-8') as data:
        data.writelines(my_data)
    return "Контакт успешно удален"

def change_contact(id, cont_data: list) -> str:
    try:
        with open(file,'r',encoding='utf-8') as data:
            my_file = data.readlines()
        for i in my_file:
            if i.split(" ")[0] == str(id):
                contact = i.split(" ")[1]
                break
        new_data = ''

        print(contact)
        return "Контакт успешно именен"
    except UnboundLocalError:
        return "Такого пользователя не найдено"


#debug
if __name__ == "__main__":
    __init__()
    #add_contact(["qwe","qwe","qwe","qwe","qwe"])
    #delete_contact(1)
    change_contact(1,["",""])