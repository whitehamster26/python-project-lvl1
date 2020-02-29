from .. import cli


def main(game, description):
    print('Welcome to the Brain Games!')
    print(description)
    name = cli.welcome_user()
    correct_answers = 0
    user_answer = None
    boolean_answers = {True: 'yes', False: 'no'}
    while correct_answers < 3:
        question, answer = game.main()
        if type(answer) == bool:
            answer = boolean_answers[answer]
            while user_answer not in boolean_answers.values():
                user_answer = input(f'Question: {question} ')
        else:
            while not str(user_answer).isdigit():
                user_answer = input(f'Question: {question} ')
            user_answer = int(user_answer)
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
