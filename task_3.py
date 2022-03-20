# задание 3 Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для
# каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
for i in range(100):
    new_str = str(i+1)
    new_list = list(new_str)
    if int(new_list[-1]) == 1 and i+1 != 11:
        print('{} процент'.format(i + 1))
    elif int(new_list[-1])>1 and int(new_list[-1])<= 4:
        if  i+1> 10 and i+1<= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))


# задание 2
# """output:
#     sum of odd elem which % 7
#     sum of odd elem(xyz..) sum(x+y+z) which % 7
#     sum of odd (elem + 17) which % 7
# """
#
# def sum_of_num(num:int):
#     res = 0
#
#     while num > 0:
#         res += num % 10
#         num //= 10
#     return res
#
# # lazy list
# list_of_odd = range(1, 1000 + 1, 2)
#
# sum_with_17:int = 0
# sum_without_17:int = 0
# for elem in list_of_odd:
#     cube = elem ** 3
#     cube_with_17 = (elem + 17) ** 3
#
#     if cube % 7 == 0:
#     if sum_of_num(cube) % 7 == 0:
#         sum_without_17 += cube
#
#     if cube_with_17 % 7 == 0:
#     if sum_of_num(cube_with_17) % 7 == 0:
#         sum_with_17 += cube_with_17
#
# print("сумма без 17:", sum_without_17)
# print("сумма c 17:", sum_with_17)
#
