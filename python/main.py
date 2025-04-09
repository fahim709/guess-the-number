import random 

number = random.randint(1, 100)
while True:
    try:
        
        person = int(input('guess the number: '))

        if person > number:
            print('Too high')
        elif person < number:
            print('Too low')
        else:
            print('Congratulations, you guessed correctly!')
            break
    except ValueError:
        print('Please enter a valid integer.')