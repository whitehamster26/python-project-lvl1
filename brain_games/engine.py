from brain_games import cli


def run(game, rounds=3):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = cli.welcome_user()
    correct_answers = 0
    user_answer = None
    while correct_answers < rounds:
        question, answer = game.start()
        user_answer = input(f'Question: {question} ')
        if user_answer == answer:
            print('Correct!')
            correct_answers += 1
        else:
            break
        user_answer = None
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{user_answer}' is wrong answer ;( Correct answer was '{answer}'.\
            ")
        print(f"Let's try again, {name}!")
