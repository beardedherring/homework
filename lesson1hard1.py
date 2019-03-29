print('Здравствуйте! Заполните, пожалуйста, вашу медицинскую карту.')
first_name = str(input('Введите имя: '))
last_name = str(input('Введите фамилию: '))
age = int(input('Введите возраст, полных лет: '))
weight = int(input('Введите вес, кг: '))
if age < 30 and weight >= 50 and weight <= 120:
    print(first_name, last_name,', возраст', age, 'л.,', 'вес', weight, 'кг' ' — Вы в хорошем состоянии')
elif age >= 30 and weight < 50 and weight > 120:
    print(first_name, last_name,', возраст', age, 'л.,', 'вес', weight, 'кг' ' — Вам нужно вести здоровый образ жизни')
elif age >=40 and weight < 50 or weight > 120:
    print(first_name, last_name,', возраст', age, 'л.,', 'вес', weight, 'кг' ' — Вам требуется врачебный осмотр')
else:
    print(first_name, last_name,', возраст', age, 'л.,', 'вес', weight, 'кг' ' — С вами что-то не то')
