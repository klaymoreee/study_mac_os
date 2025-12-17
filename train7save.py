#start block
print('''Привет! Предлагаю проверить свои знания английского!
Напиши, как тебя зовут.''')
name = input()
print(f'Привет, {name}, начинаем тренировку!')

#data block
right_counter = 0
total_score = 0
us_answers = []
quests = ['My name is Vova.', 'I am a coder.',
          'I live in Moscow.']
quests_answer_less = ['My name ____ Vova.', 'I ____ a coder.',
          'I live ____ Moscow.']
#us_answers = [input() for _ in range(len(quests))]
correct_answers = ['is', 'am', 'in']

#main block
for x in quests:
    print(quests_answer_less[quests.index(x)])
    pre_user_answer = input()
    us_answers.append(pre_user_answer)
    for y in us_answers:
        if y in correct_answers[quests.index(x)]:
            right_counter += 1
            total_score += 10
            print(f'Ответ верный!\nВы получаете 10 баллов!')
        else:
            print(f'Неправильно.\nПравильный ответ: {correct_answers[quests.index(x)]}')

#end block
print(right_counter, total_score, us_answers)