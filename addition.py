#Вычислите сумму двух чисел, записанных в d-ричной системе счисления. 1<d<36

num1, num2, d = input().split()
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def stolbik(num1,num2, d):
    answer = ""
    one = 0  # единица, которая будет играть роль в следующим сложении
    # Добавляем незначащие нули
    if len(num1) > len(num2):
        num2 = "0"*(len(num1)-len(num2))+num2
    elif len(num1) < len(num2):
        num1 = "0"*(len(num2)-len(num1))+num1

    for i in range(len(num1)):
        if one == 1: # если у нас есть единица из прошлого сложения           
            summa = (alphabet.index(num1[len(num1)-i-1]) + alphabet.index(num2[len(num2)-i-1]) + 1)

            if summa % int(d) >= 10: #преобразование числа обратно в букву если оно больше 9
                answer = alphabet[summa % int(d)] + answer
            else:
                answer = str(summa % int(d)) + answer
            one -= 1 # Вычитаем использованную единицу
            one += summa // int(d) # если число больше d, то единицу запоминаем
        else:
            summa = (alphabet.index(num1[len(num1)-i-1]) + alphabet.index(num2[len(num2)-i-1]))

            if summa % int(d) >= 10: #преобразование числа обратно в букву если оно больше 9
                answer = alphabet[summa % int(d)] + answer
            else:
                answer = str(summa % int(d)) + answer
            one += summa // int(d) # если число больше d, то единицу запоминаем
    if one == 1: # Если вычисления закончились, но осталась единица, которую мы "держим в уме"
        answer = str(one) + answer
    return answer

print(stolbik(num1,num2,d))
