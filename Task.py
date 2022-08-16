class Task():
    isRunning = False
    names = [
        'список контактов', 'расписание дел'
    ]

    command_contacts = ['посмотреть контакты','добавить контакт',
'удалить контакт','изменить контакт']
    
    default_commands = [
        'назад'
    ]

    def __init__(self):
        return