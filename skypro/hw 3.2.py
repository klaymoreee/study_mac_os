questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow", "I know! I will ___ coder!"]
answers = ["is", "am", "in", "a"]

while True:
    start = input('''Привет! 
Предлагаю проверить свои знания английского! 
Наберите "ready", чтобы начать!
: ''')
    if start != "ready":
        print('Кажется, вы не хотите играть. Очень жаль.')
    else:
        correct_count = 0
        for x in range(len(questions)):
            print(questions[x])
            answer = input('Введите ответ: ')
            if answer == answers[x]:
                print('Ответ верный!')
                correct_count += 1
            else:
                print(f'Неправильно. Правильный ответ: {answers[x]}')
        print(f'''Вот и всё! Вы ответили на {correct_count} вопросов из {len(questions)} верно, это {int((correct_count / len(questions)) * 100)}%.''')
    break


