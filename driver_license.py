

name = input('Enter your name: ')
age = int(input('Enter your age: '))
learners = input('Have you had learners for 6 months or more (yes or no): ')
MIN = 16

if(age >= MIN and learners == 'yes'):
    #eligible 
    print(f'Yes {name} you are eligible for a restricted license')
else:
    print(f'No {name} your not eligible')
