# Напишіть програму "Касир в кінотеатрі", яка буде виконувати наступне:

# Попросіть користувача ввести свій вік (можна використати константу або input()).
# - якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
#  P.S. На екран має бути виведено лише одне повідомлення! Також подумайте над варіантами, коли введені невірні дані


userinput = input('Вкажіть свій вік:')
if userinput.isalpha() or not userinput.isdigit():
    print('Помилка! Вік має бути цілим числом')
elif userinput.__contains__('-'):
    print('Вік має бути позитивним числом!')
elif userinput.__contains__(' '):
    print('Вік не має містити пробіли')
elif userinput == "":
    print('Помилка! Пустий ввід!')
elif userinput.__contains__('7'):
    print('Вам сьогодні пощастить!')
else:
    age = int(userinput)
    if age == 0:
        print('Введіть коректний вік')
    elif 0 < age < 7:
        print('Де твої батьки?')
    elif 7 < age < 16:
        print('Це фільм для дорослих!')
    elif 16 <= age <= 65:
        print('А білетів вже немає!')
    elif 120 >= age > 65:
        print('Покажіть пенсійне посвідчення!')
    elif age > 120:
        print('Cтільки не живуть!')