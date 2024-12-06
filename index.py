import json 

with open("cars.json", 'r', encoding = 'utf-8') as file: 
    data = json.load(file) # Перевод из json в python object

start = True
count = 0
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
    print(" Все записи: ".center(60,'~'))
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
    while True:
        id = input("Введите номер записи: ")
        if id.isdigit():
            id = int(id)
            break
        else: 
            print("Введите номер записи цифрой!")
        
    find = False
    for car in data:
        if id == car['id']:
            print("\n Выбранная запись: ".center(60,' '))
            print(f"""
            Номер записи: {car['id']},
            Общее название: {car['name']},
            Название производителя: : {car['manufacturer']},
            Заправляется ли бензином: {car['is_petrol']},
            Объем бака: {car['tank_volume']}
            """)
            find = True
            break
        count += 1
        

    else: 
        print("\n Запись не найдена ".center(60, "~"))

def new():
    global count
    while True:
        id = input("Введите номер записи машины: ")
        if id.isdigit():
            id = int(id)
            break
        else: 
            print("Введите номер записи машины цифрой!")
        
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

        while True:
            numb = input("Введите, заправляется ли бензином (1 - да/ 2 - нет): ")
            if numb.isdigit():
                numb = int(numb)
                if numb == 1:
                    new_is_petrol = 'да'
                    break
                elif numb == 2:
                    new_is_petrol = 'нет'
                    break
                else :
                    print("Вы должны ввести число!(1 - заправляется бензином, 2 - не заправляется)")
            else : 
                print("Введите число (1 или 2)!")


        while True:
            new_tank_volume = input("Введите объём бака(целым числом): ")
            if new_tank_volume.isdigit():
                new_tank_volume = int(new_tank_volume)
                break
            else: 
                print("Введите объём бака целым числом!")  
                    

        new_car = {
            'id': id,
            'name': new_name,
            'manufacturer':  new_manufacturer,
            'is_petrol': True if new_is_petrol.lower() == 1 else False, 
            'tank_volume':  new_tank_volume
        }

        data.append(new_car) 
        with open("cars.json", 'w', encoding = 'utf-8') as out_file: 
            json.dump(data, out_file)
        print("Машина успешно добавлена.")
    count += 1

def del_id():
    global count
    while True:
        id = input("Введите номер записи для удаления: ")
        if id.isdigit():
            id = int(id)
            break
        else: 
            print("Введите номер записи для удаления цифрой!")

    find = False  

    for car in data:
        if id == car['id']:
            data.remove(car) # Удаление 
            find = True  
            break

    if not find:
        print("Запись не найдена.")
    else:
        with open("cars.json", 'w', encoding = 'utf-8') as out_file:
            json.dump(data, out_file)
        print("Запись успешно удалена.".center(60, '=')) 
    count += 1

def exit():
    global start
    print(f"Программа завершена.Количество операций: {count}")
    start = False
        
def main():
    while start:
        menu()

        while True:
            num = input("Введите номер действия: ")
            if num.isdigit():
                num = int(num)
                break
            else: 
                print("Введите число!(цифрой)")

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
