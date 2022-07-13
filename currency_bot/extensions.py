import requests
import json
from config import keys

#самое первое число в сообщении воспринимает как сумма к конвертации
def get_amount(a):
    list_of_digits = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j].isdigit():
                list_of_digits.append(a[i])
                break
    #почему-то отдается последнее число, хотя список итерируется сначала
    #поэтому первый элемент принудительно
    if list_of_digits:
        b = list_of_digits[0].replace(',', '.')
        try:
            return float(b)
        except:
            return False
    else:
        return False

#ищем валюту в сообщении, получаем список из валют
def get_currency(t):
    list_of_currencies = []
    for i in range(len(t)):
        if 'руб' or 'дол' or 'евр' or 'юан' in t[i].lower():
            if 'руб' in t[i].lower():
                t[i] = 'рубль'
                list_of_currencies.append(t[i])
            elif 'дол' in t[i].lower():
                t[i] = 'доллар'
                list_of_currencies.append(t[i])
            elif 'евр' in t[i].lower():
                t[i] = 'евро'
                list_of_currencies.append(t[i])
            elif 'юан' in t[i].lower():
                t[i] = 'юань'
                list_of_currencies.append(t[i])
        else:
            return False
    if len(list_of_currencies) == 0:
        return False
    else:
        return list_of_currencies

class ConvertionException(Exception):
    pass

class CurrencyConverter():
    @staticmethod
    def convert(text: str):
        if get_amount(text) is False and get_currency(text) is False:
            raise ConvertionException('Укажите сумму и валюты для конвертации!')
        if get_amount(text) is False:
            raise ConvertionException('Не введена сумма конвертации!')
        if get_currency(text) is False:
            raise ConvertionException('Не указаны валюты для конвертации!')
        #https://min-api.cryptocompare.com/documentation
        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={keys[get_currency(text)[0]]}&tsyms={keys[get_currency(text)[-1]]}')
        #парсинг при помощи JSON
        total_base = json.loads(r.content)[keys[get_currency(text)[-1]]]
        return total_base
