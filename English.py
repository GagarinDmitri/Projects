print('Привет! Предлагаю проверить свои знания вншлийского!')
user_name = input('Расскажи как тебя зовут! ')
print(f'Привет, {user_name}, начинаем тренировку!')

correct_answers = 0
sum_points = 0

a1 = input('My name ___ Vova ')
if a1 == 'is':
    correct_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: is')

a2 = input('I ___ coder ')
if a2 == 'am':
    correct_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: am')

a3 = input('I live ___ Moscow ')
if a3 == 'in':
    correct_answers += 1
    print('Ответ верный!\nВы получаете 10 баллов!')
else:
    print('Неправильно.\nПравильный ответ: in')

sum_points = correct_answers * 10
user_percentage = round(correct_answers / 3 * 100, 2)

print(
    f'Вот и всё, {user_name}!\n'
    f'Вы ответили на {correct_answers} вопросов из 3 верно.\n'
    f'Вы заработали {sum_points} баллов.\n'
    f'Это {user_percentage} процентов.')
