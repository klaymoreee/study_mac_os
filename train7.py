#start block
print('''Привет! Предлагаю проверить свои знания английского!
Напиши, как тебя зовут.''')
name = input()
print(f'Привет, {name}, начинаем тренировку!')
#data block
quests_answer_less = ['My name ____ Vova.', 'I ____ a coder.',
          'I live ____ Moscow.']
correct_answers = ['is', 'am', 'in']
us_answers = []
right_counter = 0
total_score = 0

#main block
for x in quests_answer_less:
    print(x)
    us_answers.append(input())
    if us_answers[quests_answer_less.index(x)] == correct_answers[quests_answer_less.index(x)]:
        right_counter += 1
        total_score += 10
        print(f'Ответ верный!\nВы получаете 10 баллов!')
    else:
        print(f'Неправильно.\nПравильный ответ: {correct_answers[quests_answer_less.index(x)]}')

#end block
percent_result = right_counter / len(quests_answer_less) * 100
print(f'''Вот и всё, {name}!
Вы ответили на {right_counter} вопросов из 3 верно.
Вы заработали {total_score} баллов.
Это {round(percent_result)} процентов.''')