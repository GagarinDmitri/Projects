questions = ['My name ___ Vova', 'I ___ coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']
total_answers = len(questions)
correct_answers = 0
points = 0

print('Привет! Предлагаю проверить свои знания английского! Набери "ready", чтобы начать!')

if input() != 'ready':
    print('Кажется вы не хотите играть. Очень жаль!')

else:
    nca1 = 3
    while nca1 > 0:
        a1 = input(questions[0])
        if a1 == answers[0]:
            correct_answers +=1
            points += nca1
            print('Ответ верный!')
            break
        else:
            nca1 -=1
            if nca1 > 0:
                print(f'Осталось попыток: {nca1}. попробуйте ещё раз.')
            elif nca1 == 0:
                print(f'Увы, но нет. Верный ответ {answers[0]}')
    nca2 = 3
    while nca2 > 0:
        a2 = input(questions[1])
        if a2 == answers[1]:
            correct_answers +=1
            points += nca2
            print('Ответ верный!')
            break
        else:
            nca2 -=1
            if nca2 > 0:
                print(f'Осталось попыток: {nca2}. попробуйте ещё раз.')
            elif nca2 == 0:
                print(f'Увы, но нет. Верный ответ {answers[1]}')
    nca3 = 3
    while nca3 > 0:
        a3 = input(questions[2])
        if a3 == answers[2]:
            correct_answers +=1
            points += nca3
            print('Ответ верный!')
            break
        else:
            nca3 -=1
            if nca3 > 0:
                print(f'Осталось попыток: {nca3}. попробуйте ещё раз.')
            elif nca3 == 0:
                print(f'Увы, но нет. Верный ответ {answers[2]}')

    interest_answers = round(correct_answers/total_answers*100, 2)
    print(f'Вот и всё! Вы ответили на {correct_answers}'
          f' вопросов из {total_answers} верно, это {interest_answers} процентов. Вы набрали {points} баллов.')

