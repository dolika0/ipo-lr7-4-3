import json # Подключение библиотеки

with open("cars.json", 'r', encoding='utf-8') as file:  
    data = json.load(file) # Считываем из файла

count = 0 # Для подсчёта выполненных операций

while True:
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)

    while True:
        numb = input("Введите номер действия: ")
        if numb.isdigit():
            numb = int(numb)
            break
        else: 
            print("Введите число!(цифрой)")


    if numb == 1: # Выводим все записи
        print("Все записи:".center(30,'~'))
        for car in data:
            print(f"""
            Номер записи: {car['id']}, 
            Название модели: {car['name']},                       
            Название производителя: {car['manufacturer']}, 
            Заправляется ли бензином: {car['is_petrol']},    
            Объем бака: {car['tank_volume']} 
            """)
        count += 1

    elif numb == 2:
        id = input("Введите номер записи: ")
        find = False
        for car in data:
            if id == car['id']:
                print("")
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
        if not find:
            print("Запись не найдена.")


    elif numb == 3: # Добавление новой записи
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

    elif numb == 4: # Удаляем запись
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

    elif numb == 5: # Завершаем программу
        print(f"""Программа завершена.
        Кол-во операций: {count}""") 
        break


    else:
        print("Число должно быть от 1 до 5!")


        
