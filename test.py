from math import sqrt#Импортируем из модуля math функцию sqrt
try:#выполнить инструкцию перехватывая исключение
    sum_sqrt = int(input("Введите число:"))#ввод
    def sqrt_function(sum_sqrt):#функция
        sum_result = sqrt(sum_sqrt)
        return sum_result
    print(sqrt_function(sum_sqrt))#вывод
except:#исключение
    print("Что-то не так")#вывод ошибки
    print("введите число, а не букву")

    
