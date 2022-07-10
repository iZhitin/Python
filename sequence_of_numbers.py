sequence_1 = str(input("Введите последовательность неотрицательных чисел через пробел: "))
number_1 = float(input("Введите число, чтобы узнать его (или ближайшего) индекс в списке: "))

#проверка и получение списка из чисел
def check_symbols(sequence):
    for i in sequence:
        if i not in '1234567890. ':
            sequence = str(input("Введите корректную последовательность из чисел: "))
            global sequence_1
            sequence_1 = sequence
            check_symbols(sequence)
            break
    return sequence_1

sequence_2 = check_symbols(sequence_1)

#преобразование в список и проверка на наличие чисел
def catch_exception(sequence):
    try:
        b = list(map(float, sequence.split()))
    except ValueError as error:
        print('Последовательность должна соответствовать примеру: -1.0 2 3.0', '"', error, '"')
    else:
        b = list(map(float, sequence.split()))
        return b

sequence_3 = catch_exception(sequence_2)

#сортировка по возрастанию
def sorting(sequence):
    sequence.sort(key=None, reverse=False)
    return sequence

sequence_4 = sorting(sequence_3)

#для применения двоичного поиска структура должна быть отсортирована
def binary_search(sequence, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if sequence[middle] == element:
        return middle
    elif element < sequence[middle]:
        return binary_search(sequence, element, left, middle-1)
    else:
        return binary_search(sequence, element, middle+1, right)


sequence_5 = binary_search(sequence_4, number_1, 0, (len(sequence_4)-1))

print('\n', 'Полученный список:       ', catch_exception(sequence_2))
print('\n', 'Список после сортировки: ', sequence_4, '\n')
if sequence_5:
    print(' Номер позиции элемента в сортированном списке (начиная с 0),\n',
          f'который меньше введенного числа {number_1},\n',
          'а следующий за ним больше или равен этому числу: ', sequence_5)
else:
    print(f'Число {number_1} меньше {sequence_4[0]} или больше {sequence_4[len(sequence_4)-1]}')