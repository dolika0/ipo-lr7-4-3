import json 

with open("cars.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) # Перевод из json в python object

count = 0 
open = True

def menu():
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)


def all():
    global count
    for car in data:
            print(f"""
            Номер записи: {car['id']}, 
            Название модели: {car['name']},                       
            Название производителя: {car['manufacturer']}, 
            Заправляется ли бензином: {car['is_petrol']},    
            Объем бака: {car['tank_volume']} 
            """)
    count += 1

def index():
    global count
    id = int(input("Введите номер записи машины: "))
    find = False    

    for car in data:
        if id == car['id']:
            print(f"""
            Номер записи: {car['id']}, 
            Название модели: {car['name']},                       
            Название производителя: {car['manufacturer']}, 
            Заправляется ли бензином: {car['is_petrol']},    
            Объем бака: {car['tank_volume']} 
            """)
            find = True  
            break 

    count += 1

    if not find:
        print("Запись не найдена.")


def new():
    global count
    id = int(input("Введите номер машины: "))
        
    find = False
    for car in data:
        if car['id'] == id:
            find = True
            break
        
        if find: 
            print("Такой номер уже существует.")

        else:
            new_name = input("Введите название модели: ")  
            new_manufacturer  = input("Введите производителя: ")  
            new_is_petrol = input("Введите,заправляется ли бензиноом (yes/no): ")  
            new_tank_volume = float(input("Введите объём бака: "))  

            new_car = {
                'id': id,
                'name': new_name,
                'manufacturer':  new_manufacturer,
                'is_petrol': True if new_is_petrol.lower() == 'да' else False, 
                'tank_volume':  new_tank_volume
            }

            data.append(new_car) 
            with open("cars.json", 'w', encoding='utf-8') as out_file: 
                json.dump(data, out_file)
            print("Машина успешно добавлена.")
    count += 1

def del_id():
    global count
    id = int(input("Введите номер записи: "))
    find = False  

    for car in data:
        if id == car['id']:
            data.remove(car) # Удаление 
            find = True  
            break 

        if not find:
            print("Запись не найдена.")
        else:
            with open("cars.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Запись успешно удалена.") 
    count += 1

def exit():
    global count
    global open
    print(f"""Программа завершена.
    Кол-во операций: {count}""")
    open = False
        
def main():
    while open:
        menu()

        num = int(input("Введите номер действия: "))

        if num == 1:
            all()
        elif num == 2:
            index()
        elif num == 3:
            new()
        elif num == 4:
            del_id()
        elif num == 5:
            exit()
        else:
             print("Такого номера нет.")

main()
