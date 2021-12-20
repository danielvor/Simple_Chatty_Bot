# sending greatings

print('Greetings My Friend! My name is Guinti.')
print('I was created in 2021.')
print('Please, remind me your name.')
your_name = input()

# reading a name

print('What a beautiful name! Nice to meet you, {}'.format(your_name))

# asking remaiders of age

print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders and printing

value = [int(input()) for i in range(3)]
your_age = (value[0] * 70 + value[1] * 21 + value[2] * 15) % 105
print("Your age is {}; that's a good time to start programming!".format(your_age))
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here

count = 0
value = int(input())
for i in range(value+1):
    print('{} !'.format(count))
    count+=1

print('Completed, have a nice day!')
