import json # Подключение библиотеки

with open("cars.json", 'r', encoding = 'utf-8') as file:  
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

    elif numb == 2: # Выводим определенную запись

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
            print(" Запись не найдена ".center(60, "~"))


    elif numb == 3: # Добавление новой записи

        while True:
            id = input("Введите номер машины: ")
            if id.isdigit():
                id = int(id)
                break
            else: 
                print("Введите номер машины цифрой!")

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
                numb = input("Введите,заправляется ли бензином (1 - да/ 2 - нет): ")
                if numb.isdigit():
                    numb = int(numb)
                    if numb == 1:
                        new_is_petrol = 'да'
                        break
                    elif numb == 2:
                        new_is_petrol = 'нет'
                        break
                    # else :
                    #     print("Введите одно из предложенных чисел!")
                else :
                    print("Вы должны ввести число!(1 - заправляется бензином, 2 - не заправляется)")
                
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
                'is_petrol': True if new_is_petrol.lower() == 'да' else False, 
                'tank_volume':  new_tank_volume
            }

            data.append(new_car) 
            with open("cars.json", 'w', encoding='utf-8') as out_file: 
                json.dump(data, out_file)
            print("Машина успешно добавлена.")

        count += 1

    elif numb == 4: # Удаляем запись
        id = int(input("Введите номер записи для удаления: "))
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
        print(f"Программа завершена.Кол-во операций: {count}") 
        break


    else:
        print("Число должно быть от 1 до 5!")
