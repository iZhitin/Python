while True:
    quantity = int(input("Сколько билетов Вы хотите приобрести на мероприятие? "))
    q = 0
    full_cost = 0
    while q != quantity:
        q += 1
        age = int(input(f"Каков возраст посетителя {q}? "))
        if age < 18:
            cost = 0
        elif age >= 25:
            cost = 1390
        else:
            cost = 990
        full_cost += cost
    if q > 3:
        full_cost *= 0.9
        print(f"Стоимость вашего заказа с учетом скидки 10% за {q} бил. составляет {full_cost} руб.!")
    else:
        print(f"Стоимость заказа за {q} бил. составляет {full_cost} руб.!")

    exit = input("Введите 'q' и нажмите enter для выхода! ")
    if exit == "q":
        break
