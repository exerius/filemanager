import os
def make(name):
    if len(name) == 1:
        os.makedirs(name[0])
    else:
        for i in name:
            os.makedirs(i)


def read():
    command = str(input('Введите команду'))


def remove(name):
    if len(name) == 1:
        os.remove(name[0])
    else:
        for i in name:
            os.remove(i)


def go(name):
    if len(name)>1:
        print('Вы ввели что-то не то')
    else:
        os.chdir(name[0])


def create(name):
    for i in name:
        file = open(i, 'w')
        file.close()


def write(name):
    if len(name) > 1:
        print("вы ввели что-то не то")
    else:
        with open(name, "a+") as file:
            addition = input("Введите текст")
            file.write(addition)

def delete(name):
    for i in name:
        os.rmdir(i)


def move(name, new_name):
    if type(name) != str:
        print("Вы ввели что-то не то")
    else:
        os.rename(name, new_name)

def interpret(command):
    command = command.split()
    if command[0] == 'make':
        make(command[1::])
    elif command[0] == 'remove':
        remove(command[1::])
    elif command[0] == 'go':
        go(command[1::])
    elif command[0] == 'create':
        create(command[1::])
    elif command[0] == 'write':
        write(command[1::])
    elif command[0] == 'read':
        read(command[1::])
    elif command[0] == 'delete':
        delete(command[1::])
    elif command[0] == 'move':
        move(command[1::])
    elif command[0] == 'rename':
        move(command[1::])
    else:
        print('Вы ввели что-то не то')



