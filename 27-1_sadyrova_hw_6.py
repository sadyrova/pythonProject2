import re

with open('MOCK_DATA.txt', encoding='utf-8') as file:
    content = file.read()
    #print(content)

    # "[А-Я][а-я]+\s+[А-Я]\.[А-Я]\."
    name_list= re.findall(r"(?:[A-Z][a-z-]+\s[A-Z][a-z]+|[A-Z][a-z-]+\s[A-Z][\'][A-Z][a-z]+)", content)
    #name_list = re.findall(r"(?:[A-Z][a-z-]+\s[A-Z][a-z]+\s[A-Z][a-z]+)", content)

    with open("name_file.txt", "w") as file:
        for line in name_list:
            file.write(line + '\n')

    email_list = re.findall(r'(?:[\w .-]+\@[\w.-]+\.[\w.]+)', content)
    with open("email_file.txt", "w") as file:
        for line in email_list:
            file.write(line + '\n')

    file_name_list = re.findall(r'(?:[A-Z][\w]+\.[a-z]+)', content)
    with open("file_name.txt", "w") as file:
        for line in file_name_list:
            file.write(line + '\n')

    color_list = re.findall(r'(?:[#]\w*)', content)
    with open("color_file.txt", "w") as file:
        for line in color_list:
            file.write(line + '\n')


while True:
    print("\nВыберите из меню")
    print("1. Считать имена и фамилии")
    print("2. Считать все емайлы")
    print("3. Считать названия файлови")
    print("4. Считать цвета")
    print("5. Exit")
    choice = int(input("Введите выбор:"))

    if choice == 1:
        print(f'{len(name_list)}: {name_list}')

    elif choice == 2:
        print(f'{len(email_list)}: {email_list}')

    elif choice == 3:
        print(f'{len(file_name_list)}: {file_name_list}')

    elif choice == 4:
        print(f'{len(color_list)}: {color_list}')

    elif choice == 5:
            break


