import shutil, os, zlib, pathlib, hashlib
from sys import platform


def read_command():
    command = str(input('Введите команду'))
    return command


def unarchive(name):
    path = pathlib.Path(name).resolve()
    if path.is_relative_to(home_dir):
        try:
            shutil.unpack_archive(path)
        except FileNotFoundError:
            print("Нет такого архива")
    else:
        print("у вас папке такого нет")


def archive(name, type, dir):
    if pathlib.Path(dir).resolve().is_relative_to(home_dir):
        if (type != "zip") and (type != "tar"):
            print("Неподдерживаемый формат архива")
        else:
            try:
                shutil.make_archive(name, type, dir)
            except FileNotFoundError:
                print("Папка %s не найдена" % dir)
            except:
                print("Вы ввели что-то не то")
    else:
        print("у вас папке такого нет")


def move(names, dest):
    dest = pathlib.Path(dest).resolve()
    for i in range(len(names)):
        names[i] = pathlib.Path(names[i]).resolve()
    for i in range(len(names)):
        shutil.move(names[i], dst=dest)


def copy(names, dest):
    dest = pathlib.Path(dest).resolve()
    for i in range(len(names)):
        names[i] = pathlib.Path(names[i]).resolve()
    for i in range(len(names)):
        shutil.copy2(names[i], dst=dest)


def delete(names):
    for i in range(len(names)):
        names[i] = pathlib.Path(names[i]).resolve()
    for i in names:
        try:
            shutil.rmtree(i)
        except:
            os.remove(i)


def go(path):
    path = pathlib.Path(path).resolve()
    if path.is_relative_to(home_dir):
        os.chdir(path)
    else:
        print("у вас папке такого нет")


def make(name):
    for i in range(len(name)):
        name[i] = pathlib.Path(name[i])
    for i in range(len(name)):
        if not name[i].is_absolute():
            os.mkdir(name[i])


def create(name):
    for i in range(len(name)):
        name[i] = pathlib.Path(name[i])
    for i in range(len(name)):
        if not name[i].is_absolute():
            file = open(str(name[i]), "w")
            file.close()


def rename(name1, name2):
    name1 = pathlib.Path(name1).resolve()
    name2 = pathlib.Path(name2)
    if name1.is_relative_to(home_dir) and not name2.is_absolute():
        os.renames(name1, name2)
    else:
        print("у вас папке такого нет")


def read(file):
    file = pathlib.Path(file).resolve()
    if file.is_relative_to(home_dir):
        with open(file, "r") as f:
            for i in f:
                print(i)


def write(file):
    file = pathlib.Path(file).resolve()
    if file.is_relative_to(home_dir):
        with open(file, "a+") as f:
            addition = input()
            f.write(addition)
    else:
        print("у вас папке такого нет")


def interpret(command):
    command = command.split()
    if command[0] == 'make':
        make(command[1::])
    elif command[0] == 'delete':
        delete(command[1::])
    elif command[0] == 'go':
        go(command[1])
    elif command[0] == 'copy':
        copy(command[1:-1], dest=command[len(command)-1])
    elif command[0] == 'create':
        create(command[1::])
    elif command[0] == 'write':
        write(command[1])
    elif command[0] == 'read':
        read(command[1])
    elif command[0] == 'move':
        move(command[1:-1], dest=command[len(command)-1])
    elif command[0] == 'rename':
        rename(command[1], command[2])
    elif command[0] == 'archive':
        archive(command[1], command[2], command[3])
    elif command[0] == 'unarchive':
        unarchive(command[1])
    else:
        print('Вы ввели что-то не то')


logged = False
settings = str(pathlib.Path.home())+str(pathlib.Path("/.filemanager/settings.txt"))
action = input("Login or register?\n")
if action == "login":
    login = input("Введите логин ")
    password = input("Введите пароль ")
    with open(settings, "r") as file:
        for i in file:
            if login in i.split(";"):
                line = i.split(";")
                if hashlib.sha256(password.encode()).hexdigest() == line[1]:
                    home_dir = pathlib.Path(line[2])
                    go(home_dir)
                    logged = True
                else:
                    print("Пароль неверен")
elif action == "register":
    login = input("Введите логин ")
    password = hashlib.sha256(input("Введите пароль ").encode()).hexdigest()
    home_dir = pathlib.Path(input('Введите путь до папки пользователя '))
    line = ";".join([login, password, str(home_dir)])+";\n"
    with open(settings, "a") as file:
        file.write(line)
    try:
        make([home_dir])
    except FileExistsError:
        pass
    go(home_dir)
    logged = True
if logged:
    while True:
        command = read_command()
        if command != 'exit':
            interpret(command)
        else:
            break
else:
    print("Логин или пароль неверны")