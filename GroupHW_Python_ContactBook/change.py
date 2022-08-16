#Модуль, отвечающий за изменение контактов (Удаление, добавление, изменение)
from functools import reduce

global file
file = 'GroupHW_Python_ContactBook\phones.txt'

def add_contact(cont_data: list) -> str:
    try:
        with open(file, 'r', encoding='utf-8') as data:
            my_data = data.readlines()
        last_id = my_data[len(my_data) - 1].split('\t')[0]
        tmp_contact = f"{int(last_id) + 1}\t{cont_data[0]}\t{cont_data[1]}\t\
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
        tmp_list.append(i.split("\t"))
    my_data.clear()
    my_data.append(title)
    for i in tmp_list:
        i[0] = str(counter)
        my_data.append(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}")
        counter += 1
    
    with open(file,'w',encoding='utf-8') as data:
        data.writelines(my_data)
    return "Контакт успешно удален"

def change_contact(id, cont_data: list) -> str:
    try:
        with open(file,'r',encoding='utf-8') as data:
            my_file = data.readlines()

        for i in my_file[1:]:
            if int(split_num(i)[0]) == int(id):
                contact = split_num(i)[1].split("\t")
                break
        print(contact)
        new_info = ''

        for i in range(len(contact)):
            if str(cont_data[i]) == '':
                new_info += contact[i]
                if i != len(contact)-1:
                    new_info += "\t"
            else:
                new_info += cont_data[i]
                if i != len(contact)-1:
                    new_info += "\t"
                    
        my_file[id] = f"{id}\t{reduce(lambda x, y:x+y, new_info)}\n"
        print(my_file)
        with open(file, 'w', encoding='utf-8') as data:
            data.writelines(my_file)
        return "Контакт успешно именен"
    except UnboundLocalError:
        return "Такого пользователя не найдено"

def split_num(inpt_str: str) -> list:
    '''
    Метод, возвращающий id и остальную инфу раздельно
    '''
    result = [inpt_str[:inpt_str.find("\t")], inpt_str[inpt_str.find("\t")+1:]]
    print(result)
    return result
#debug
if __name__ == "__main__":
    #add_contact(["qwe","qwe","qwe","qwe","qwe"])
    delete_contact(1)
    #change_contact(1,["","","qwe","qwe","qwe"])
    print(1)