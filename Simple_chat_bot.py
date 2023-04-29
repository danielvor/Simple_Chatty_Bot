# import sleep function from time module
from time import sleep


# Intro to the program
def greet(bot_name, birth_year):
    print('Hi, there! My name is ' + bot_name + '...')
    sleep(2) # wait 2 seconds
    print('I was created in ' + birth_year + '.')
    sleep(2) # wait 2 seconds

# Greets the user and asks for their name
def remind_name():
    print('Please, remind me your name.')    
    name = input()
    print('What a beautiful name you have, ' + name + ' !!!')
    sleep(2) # wait 2 seconds

# Counts to any number the user wants
def count():
    print('Like a robot I can count to any number you want.')
    sleep(2) # wait 2 seconds
    print('Please, tell me a number.')
    num = int(input())
    current = 0
    while current <= num:
        if current < num:
            print(current, ',', end=' ')
        else :
            print(current, end=" ! \n")
        current += 1
    sleep(2) # wait 2 seconds

# Asks the user who create Guinti
def juliana_leal():
    # Quizz
    print("Quick quizz.")
    sleep(2) # wait 2 seconds
    print('Who create Guinti?')
    sleep(2) # wait 2 seconds
    questions = ['alternatives:', '1. Juliana Leal', '2. Batman',
                '3. Leonardo Ferreira', '4. Daniel Rodrigues']
    
    for q in questions:
        if q == questions[-1]:
            print(q)
        else:
            print(q, end=" ")
    
    while input() != '1':
        print('Please, try again.')
    print('Correct, Guinte was create by' + questions[1][2:] + '!')
    sleep(2) # wait 2 seconds

def end():
    print('Congratulations, have a nice day!')

greet('Guinti', '2020')
remind_name()
count()
juliana_leal()
end()
