# тип цыкла while
# while условие:
#     # блок если да
# count = 0
# while count < 10:
#     print("this is while loop", count)
#     count += 1
# строки и методы строк
# форматирование строк
# case = 1
# result = "qwe"
# # print(f"Выпало чило:{case} с результатом:{result} ")
#
# dirname = "home"
# filnema = "test.py"
# path = f"{dirname}/{filnema}"
# # print(path)
# # литералы строк
# my_str_1 = "qwerty"
# my_str_2 = 'asdfg'
# my_str_3 = ''' zxcvbn'''
# my_str_4 = """ qazsxw"""
#
#
# index = -1 #последний с конца стоки
# symbol = my_str_1[index]
# # print(symbol)
#
# string_len = len(my_str_1)
# print(string_len, my_str_1[string_len -1 ])
# срез строки
# my_str_1 = "I'm Qwerty"
# # new_str = my_str_1[40:70] ошибки нет
# # new_str = my_str_1[1:-1] 'm Qwerty
# # new_str = my_str_1[-50:-1] I'm Qwerty
# # new_str = my_str_1[:] все строка
# # new_str = my_str_1[:-3] от начала и до
# # new_str = my_str_1[2:] от ... и до конца строки
# index = 5
# new_str = my_str_1[:index] + "K" + my_str_1[index +1:] #замена символа
#
# print(new_str)

# my_str_1 = "I'm Qwerty"

# new_str = my_str_1[1:-1:3] # шаг среза (каждые 3)
# new_str = my_str_1[::2] # на четных мест
# new_str = my_str_1[1::2] # на нечетных местах в троке
# new_str = my_str_1[::-1] # читает в обратнуб сторону (с конца) РАЗВОРОТ СТРОКИ


# print(new_str)

# my_str_1 = " I'm Qwerty"
#
# if my_str_1[-1] == "a":
#     print(f"'a' on last position in {my_str_1}")
# else:
#     print(f"'a' not on last position in {my_str_1}")

# my_str_1 = "I'm Qwerty"

# for symbol in my_str_1: # строка -интерируемый обьект
#     # if (symbol not in "EYUIAeyuioa") and symbol.isalpha() and symbol.isupper():
#     if (symbol.lower() not in "eyuioa") and symbol.isupper():
#         print(symbol)
#
# my_str_1 = "I'm Qwerty"
# # for symbol in my_str_1:
# #     print(f"symbol: '{symbol}'--> {ord(symbol)}")
# for index in range(ord('z') + 1):
#     print(f"index: {index} --> '{chr(index)}'")


# пиведение типов

# value= 0
# value_bool = bool(value) #true кроме значения 0 --> False
# print(value_bool)

# value= 0.0
# value_bool = bool(value) #true кроме значения 0.0 --> False
# print(value_bool)


# value= "qwerty"
# value_bool = bool(value) #true кроме значения ПУСТОЙ строки --> False
# print(value_bool)
#########################################################################

# case = 3
# if case == 6:
#     print("Победил Вася!")
# elif case == 1:
#     print("победил Петя!")
# else:
#
#     print("Все проиграли!")

# case = input("кинь кубик:")   # всегда СТРОКА str
# # case = int(case)
#
# print(case, type(case))
# if case == 6:
#     print("Победил Вася!")
# elif case == 1:
#     print("победил Петя!")
# else:
#     print("Все проиграли!")


# from random import randint
# case = randint(1, 6)
# print("Выпало число:", case)
# # case = int(case)
#
# if case == 6:
#     print("Победил Вася!")
# elif case == 1:
#     print("победил Петя!")
# else:
#     print("Все проиграли!")
# if case > 3:
#     result= case ** 2
# else:
#     result = - case
#
# result = case ** 2 if case > 3 else - case # тернарный оператор
#
# print("выпало чилов:", case, "Результат:", result)


# if условие:
#     блок, если ДА (условие 1)
# elif условие 2
# else:
#   блок, если НЕТ


# temp = 0.1
#
# if temp > 0:
#     print("Можно шапку не надевать")
#     print("temp:",temp )
#
# else:
#     print("Надень шапку!")
#     print("End of else")


# my_value = 7
# my_bool = my_value % 3 == 0
# my_bool1 = my_value % 2 == 0
# print(not my_bool and not my_bool1)


#
# a= 'Hello,"A"'
# b= a
# c= 'Hello,"B"'
# b= c
# c= a
# a=b
# print(a)


# valueX= 2
# valueY= '4'
# valueX= str(valueX)
#
# print(valueX + valueY)


# приведения типов
#
# value= "-19"
# new_value = float(value)
# print(new_value, type(new_value))


# some_value= 4
# bool_value_1 = (2 != some_value)
# bool_value = bool_value_1

# print(bool_value, type(bool_value))


# value_1 = "25"
# value_2 = "2"
#
#
# #value= value_1 % value_2
# #value= value_1 ** value_2
# value= value_1 + value_2
#
# print(value)


# value = "100"
# value = 100
# first = "qwe"
# second = 1
# value = first
# first = second
# second = value
#
# print(first, second)


# print ("hello World!")
# comment
# print ("hello World!")

# print (123 * 2, 456, "789", "qwerty")
# print (12 - 3)
# print (23 + 5)
