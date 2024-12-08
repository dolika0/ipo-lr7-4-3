import json 
with open("cars.json", 'r', encoding = 'utf-8') as file: 
    data = json.load(file) # Перевод из json в python object

def validation(prompt):
    while(True):
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else: 
            print("Введите необходимую информацию числом!")
            
        
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
    id = validation("Введите номер записи для вывода: ")
        
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
            count += 1
            break
    if find == False: 
        print("\n"," Запись не найдена ".center(60, "~"))


def new():
    global count
    if data:
        id = max(int(car['id']) for car in data) + 1 
    else: id = 1
    
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
            num = validation("Введите, заправляется ли бензином (1 - да, 2 - нет): ")
            if num == 1 or num == 2:
                new_is_petrol = True if num == 1 else False 
                break 
            else:
                print("Введите 1, если заправляется бензином. Если не заправляется, введите 2.")

        new_tank_volume = validation("Введите объём бака(целым числом): ")

        new_car = {
            'id': id,
            'name': new_name,
            'manufacturer':  new_manufacturer,
            'is_petrol': new_is_petrol, 
            'tank_volume':  new_tank_volume
        }

        data.append(new_car) 
        with open("cars.json", 'w', encoding = 'utf-8') as out_file: 
            json.dump(data, out_file)
        print("Машина успешно добавлена.")
    count += 1

def del_id():
    global count
    id = validation("Введите номер записи для удаления : ")

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
    
        num = validation("Введите номер действия: ")
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
