
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow", "I know! I will ___ coder!"]
answers = ["is", "am", "in", "a"]

while True:
    start = input('Привет!\nПредлагаю проверить свои знания английского!\nНаберите "ready", чтобы начать!\n: ')
    if start != "ready":
        print('Кажется, вы не хотите играть. Очень жаль.')
    else:
        correct_count = 0
        for x in range(len(questions)):
            miss_count = 2
            print(questions[x])
            answer = input('Введите ответ: ')
            if answer == answers[x]:
                print('Ответ верный!')
                correct_count += 1
            else:
                while miss_count > 0:
                    try_again_answer = input(f'Осталось попыток: {miss_count}, попробуйте еще раз!\n: ')
                    if try_again_answer != answers[x]:
                        miss_count -= 1
                        continue
                    else:
                        print('Ответ верный!')
                        break
                print(f'Увы, но нет. Верный ответ: {answers[x]}')
        print(f'''Вот и всё! Вы ответили на {correct_count} вопросов из {len(questions)} верно, это {int((correct_count / len(questions)) * 100)}%.''')
    break


