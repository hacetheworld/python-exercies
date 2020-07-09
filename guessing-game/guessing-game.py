import random
randNum = random.randint(1, 10)
print(randNum)

while (True):
    userNum = int(input('Guess the number'))
    if(randNum == userNum):
        print('you win')
        break
    elif(abs(randNum-userNum) <= 5):
        print('too close')
    else:
        print('too away')
    print('try again')
