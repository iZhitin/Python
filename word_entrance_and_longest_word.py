def scaner_amount_of_word_entrance(doc):
	"""Сканер проверяет текст и выдает слово с максимальным числом вхождений"""
	# удаление специальных символов из текста
	for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
		doc = doc.replace(i, '')
	# замена переносов строк на пробелы
	new_doc = doc.replace('\n', ' ')
	# создание списка по пробелам
	list_1 = list(map(str, new_doc.split(' ')))
	# добавление элементов длиной больше 2 из списка 1 в список 2
	list_2 = []
	for i in range(len(list_1)):
		if len(list_1[i]) > 2:
			list_2.append(list_1[i])

	# возвращение элемента с максимальным числом вхождений (если их несколько, то - первый)
	entries = []
	for i in range(len(list_2)):
		# в список добавляется количество вхождений данного элемента в списке 2
		entries.append(list_2.count(list_2[i]))
	# print(entries)

	# вывод из списка 2 элемента с индексом, равным индексу списка с подсчетом вхождений
	return list_2[entries.index(max(entries))]


def scaner_of_max_eng_word(doc):
	"""Сканер проверяет текст и выдает слово максимальной длины, содержащее латинские буквы"""
	# удаление специальных символов из текста
	for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
		doc = doc.replace(i, '')
	# замена переносов строк на пробелы
	new_doc = doc.replace('\n', ' ')
	# создание списка по пробелам
	list_1 = list(map(str, new_doc.split(' ')))

	# латинский алфавит с низким и верхним регистром
	full_alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

	# если в слове есть хотя бы одна латинская буква, то слово добавляется в словарь
	eng_list = []
	for i in range(len(list_1)):
		for j in full_alpha:
			if j in list_1[i]:
				eng_list.append(list_1[i])
				break

	# возвращается самое длинное слово из словаря
	return max(eng_list, key=len)


# проверка текста написанными функциями
text = "Предлоги: на, из, в, от, с; склонение притяжательных местоимений: мой твой его его " \
	   "Prepositions: on, from, to, from, with; declension of possessive pronouns: my, your, his, his"

print("Первое самое часто встречающееся слово текста: " + scaner_amount_of_word_entrance(text))
print("Первое самое длинное слово с латинской буквой в тексте: " + scaner_of_max_eng_word(text))


# проверка текстового файла написанными функциями
myFile = input('Введите имя файла c расширением из текущего каталога: ')
with open(myFile, 'rt', encoding='utf8') as f:
	text = f.read()
	print(scaner_amount_of_word_entrance(text), scaner_of_max_eng_word(text))
	
