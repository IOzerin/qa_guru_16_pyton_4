# Заводим словари

d = {
    "key": "value",
    "sekond key": "second value"
}

user1 = {
    "name": "Vasya",
    "age": 18,
    "id": 1024
}

user2 = {
    "name": "Petya",
    "age": 20,
    "id": 1025
}

users = {
    1024: user1,
    1025: user2
}

print(user1["name"])
print(user2["name"])

users[1027] = {"name": "Katya", "age": 19, "id": 1027}



# Функции словарей
# Возвращает список пар ключей и значений
users.items()

# Возвращает список значений
users.values()

# Возвращает список ключей
users.keys()


print(users[1025])
print(users.get(1025))


# Отличие этих двух типов обращения заключается в том,
# что при обращении к несуществующему значению
# print(users[1026]) приведет к ошибке, а
print(users.get(1026))
# отобразит специальный тип данных None, но вместо None
# можно отобразить собственное заданное значение по умолчанию
print(users.get(1026, {"name": "default user"}))

print(users)