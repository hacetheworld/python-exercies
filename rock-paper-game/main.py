print('---Rock----')
print('---Papper----')
print('---Scissors----')
player1Choice = input("Enter Player 1's choice : ")
player2Choice = input("Enter Player 2's choice : ")
print('Shoot!!!!')
print('Results:')
if(player1Choice == 'scissors'):
    print('Player 1 wins :)')
elif(player2Choice == 'scissors'):
    print('Player 2 wins :)')
else:
    print('Match draw')
