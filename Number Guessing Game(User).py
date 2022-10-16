from random import randint
def baby(a):
    guess=0
    score=0
    random_num=randint(1,a)
    while (guess!=random_num ):
        score=score+1
        guess =int(input('Enter your guess '))
        if guess>a or guess<1:
            print('PLEASE ENTER WITHIN THE RANGE')
        if guess>random_num:
            print('Sorry the number is lower than this try again\n')
        elif guess<random_num:
            print('Sorry the number is higher than this try again\n')
            
    print(f'Yay!!! You Guessed the correct number that is {random_num}')
    print(f'You guessed the number right in {score} attempts')

    return score

def cond():
    print('Do you wanna continue \nEnter (1) if yes else (2) for no')
    g=int(input())
    if g==1:
        x=int(input('Do you want to level up if no enter 10 else enter your upper limit'))
        new_score=baby(x)
        if new_score<old_score:
            print(f'your High score = {new_score}')
        else:
            print(f'High Score ={old_score}')


old_score = baby(10)
cond()







