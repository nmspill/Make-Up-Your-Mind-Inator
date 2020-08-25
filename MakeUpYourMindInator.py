import random
import os
import time


def intro_animation():
    intro = 'Welcome to the Make-Up-Your-Mind-Inator!'
    for c in intro:
        print(c, end='', flush=True)
        time.sleep(.05)


def number_of_choices_animation():
    sentence = 'Enter the number of choices: '
    invalid_number = 'Please enter an integer'
    valid_number = False
    while not valid_number:
        for c in sentence:
            print(c, end='', flush=True)
            time.sleep(.05)

        number = input()

        try:
            number = int(number)
            valid_number = True

        except ValueError:
            for c in invalid_number:
                print(c, end='', flush=True)
                time.sleep(.05)
            print('\n')

    return number


def options_animation(num_choice):
    sentence = 'Option ' + str(num_choice) + ': '
    for c in sentence:
        print(c, end='', flush=True)
        time.sleep(.05)

    return input()


def calculating_animation(text, delay=.5):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(.05)
    n_dots = 0

    for loop in range(0, 7):
        if n_dots == 3:
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            n_dots = 0
        else:
            print(end='.', flush=True)
            n_dots += 1
        time.sleep(delay)
    print(end='\b\b\b\b\b\b\b\b\b\b\b\b\b\b', flush=True)
    print(end='                 ', flush=True)


def answer_animation(answer):
    reveal = "The Make-Up-Your-Mind-Inator Chooses"
    for c in reveal:
        print(c, end='', flush=True)
        time.sleep(.05)
    for c in range(0, 3):
        print(".", end='', flush=True)
        time.sleep(.5)

    print(' ', end='')
    for c in answer:
        print(c.upper(), end='', flush=True)
        time.sleep(.025)

    print('!')


def outro_animation():
    outro = "Type 'Yes' to use the Make-Up-Your-Mind-Inator again! "
    for c in outro:
        print(c, end='', flush=True)
        time.sleep(.05)

    return input()


def Make_Up_Your_Mind_Inator():

    options = []
    choosing = True
    num_choice = 1

    while choosing:
        if num_choice == 1:
            intro_animation()
            time.sleep(1)
            print('\n')
            num_of_choices = number_of_choices_animation()
            print('\n')

        while num_of_choices >= num_choice:
            choice = options_animation(num_choice)
            options.append(choice)
            num_choice += 1

        print('\n')
        calculating_animation('Calculating')
        print('\r', end='')

        answer_animation(options[random.randint(0, num_of_choices-1)])
        time.sleep(1)

        print('\n')
        done = outro_animation()

        if done.lower() == 'yes':
            options.clear()
            num_choice = 1
            os.system('cls')
        else:
            choosing = False


Make_Up_Your_Mind_Inator()
