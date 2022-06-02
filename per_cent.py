per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете положить под процент: "))
dep = list(per_cent.values())
deposit = [((i*money)/100) for i in dep]
print("Максимальная сумма, которую вы можете заработать — " + str(max(deposit)))