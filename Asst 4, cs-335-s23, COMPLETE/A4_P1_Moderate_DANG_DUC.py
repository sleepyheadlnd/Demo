name = "DANG_DUC"
header1 = "CS-335, Spring 2023"
header2 = "A4_P1_Moderate"


#=======================================================================
# divisor_game(n, player1, player2)
#
# Moderates the divisor game starting with postive integer n 
# between player1 and player2 (both are strings of their names).
#                                                           
# This function has no return value.
#=======================================================================

def divisor_game(n, player1, player2):

   numberList =[]
   for i in range(1,n+1):
      if (n % i == 0):
         numberList.append(i)
   print(f'\nHere are the remaining numbers: {numberList}')
   invalid = True
   while len(numberList) != 0:
      j=0
      x=0
      p1= int(input(f'{player1}, pick a number from the list above: '))
      while p1 not in numberList:
         p1 = int(input(f'{player1}, pick something that is IN the list: '))

      if(p1 == n):
         print(f'\n{player1}, you lose! {player2}, you win!')
         break
      else:
         while p1 in numberList:
            if (p1 % numberList[j] == 0):
               del numberList[j]
            else:
               j+=1
      print(f'\nHere are the remaining numbers: {numberList}')

      p2 = int(input(f'{player2}, pick a number from the list above: '))
      while p2 not in numberList:
         p2 = int(input(f'{player2}, pick something that is IN the list: '))

      if (p2 == n):
         print(f'\n{player2}, you lose! {player1}, you win!')
         break
      else:
         while p2 in numberList:
            if (p2 % numberList[x] == 0):
               del numberList[x]
            else:
               x += 1
      print(f'\nHere are the remaining numbers: {numberList}')




#=======================================================================
# Main program below (do not alter!)
#=======================================================================

print()
print(name)
print(header1)
print(header2)
print()


print("Welcome to the Divisor Game!")

playAgain = 'y'
testNum = 0

while playAgain[0] in ['y', 'Y']:

   print("\n=========================================================")
   testNum += 1
   print(f'Test case {testNum}:')
   
   player1 = input("\nPlayer 1, enter your name:  ")
   player2 = input("Player 2, enter your name:  ")
   n = int(input("\nEnter positive integer n:  "))

   divisor_game(n, player1, player2)
   
   playAgain = input("\nDo you want to play again? (y/n):  ")
   

print("\nBye!")
   



