'''
В первом поле числа от 3 до 20 случайным образом.
Во второе нужно подобрать пары чисел друг за другом,
чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.
Все пароли для чисел от 3 до 20 (для сверки):

3 - 12
4 - 13
5 - 1423
6 - 121524
7 - 162534
8 - 13172635
9 - 1218273645
10 - 141923283746
11 - 11029384756
12 - 12131511124210394857
13 - 112211310495867
14 - 1611325212343114105968
15 - 1214114232133124115106978
16 - 1317115262143531341251161079
17 - 11621531441351261171089
18 - 12151811724272163631545414513612711810
19 - 118217316415514613712811910
20 - 13141911923282183731746416515614713812911

Отдельно по числам, для большего понимания:
3 - 1+2
4 - 1+3
5 - 1+4 2+3
6 - 1+2 1+5 2+4
7 - 1+6 2+5 3+4
8 - 1+3 1+7 2+6 3+5
...
18 - 1+2 1+5 1+8 1+17 2+4 2+7 2+16 3+6 3+15 4+5 4+14 5+13 6+12 7+11 8+10
19 - 1+18 2+17 3+16 4+15 5+14 6+13 7+12 8+11 9+10
20 - 1+3 1+4 1+9 1+19 2+3 2+8 2+18 3+7 3+17 4+6 4+16 5+15 6+14 7+13 8+12 9+11
Примечания:
Можно использовать как цикл for, так и цикл while
Первое число не входит в одно из чисел пары
Пары чисел подбираются от 1 до 20 для текущего числа.
'''

def get_password (n):
    result = ''
    for i in range (1, n):
        for j in range (i+1, n):
            if n % (i+j) == 0:
                result += str(i) + str(j)
    return result

number = 0
while number < 3 or number > 20:
    number = int(input('Введите число от 3 до 20: '))
password = get_password (number)
print(f'Пароль для числа {number}: {password}')