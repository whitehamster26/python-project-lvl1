from brain_games import cli


def run(game, rounds=3):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = cli.welcome_user()
    for round in range(rounds):
        question, answer = game.start()
        user_answer = input(f'Question: {question} ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;( Correct answer was '{answer}'.\
            ")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
