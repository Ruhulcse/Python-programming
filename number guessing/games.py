import random
secret=random.randint(1,20)
for guessTaken in range(1,7):
    print('take a guess')
    guess=int(input())
    if guess<secret:
        print('your number is too low')
    elif guess>secret:
        print('your number is hight ')
    else:
        break;
if guess==secret:
    print('Congratulation you have won the game')
else:
    print('sorry you have loss the the game')
    print('my number was',str(guessTaken)+'guesses!')
