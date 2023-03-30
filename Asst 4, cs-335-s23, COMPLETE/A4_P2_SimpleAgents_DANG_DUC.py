name = "DANG_DUC"
header1 = "CS-335, Spring 2023"
header2 = "A4_P2_SimpleAgents"

import random

#=======================================================================
# divisor_game_agent(n, name, turnNum, agent)
#
# Mediates the divisor game starting with postive integer n 
# between a human named "name" and agent "agent", which is a function that takes a list
# of the remaining divisors and returns one of them.
#                                                           
# turnNum = 1 if the human wants to go first, 2 if the human wants to go second.
#

def divisor_game_agent(n, name, turnNum, agent):
   numberList = []
   for i in range(1, n + 1):
      if (n % i == 0):
         numberList.append(i)

   print(f'\nHere are the remaining numbers: {numberList}')
   invalid = True
   while len(numberList) != 0:
      j = 0
      x = 0
      if turnNum == 1:
         p1 = int(input(f'{name}, pick a number from the list above: '))
         while p1 not in numberList:
            p1 = int(input(f'{name}, pick something that is IN the list: '))

         if (p1 == n):
            print(f'\n{name}, you lose! Agent, you win!')
            break
         else:
            while p1 in numberList:
               if (p1 % numberList[j] == 0):
                  del numberList[j]
               else:
                  j += 1
         print(f'\nHere are the remaining numbers: {numberList}')

         p2 = agent(numberList)
         print(f'Agent picked {p2}')

         if (p2 == n):
            print(f'\nAgent, you lose! {name}, you win!')
            break
         else:
            while p2 in numberList:
               if (p2 % numberList[x] == 0):
                  del numberList[x]
               else:
                  x += 1
         print(f'\nHere are the remaining numbers: {numberList}')
      else:
         p2 = agent(numberList)
         print(f'Agent picked {p2}')

         if (p2 == n):
            print(f'\nAgent, you lose! {name}, you win!')
            break
         else:
            while p2 in numberList:
               if (p2 % numberList[x] == 0):
                  del numberList[x]
               else:
                  x += 1
         print(f'\nHere are the remaining numbers: {numberList}')

         p1 = int(input(f'{name}, pick a number from the list above: '))
         while p1 not in numberList:
            p1 = int(input(f'{name}, pick something that is IN the list: '))

         if (p1 == n):
            print(f'\n{name}, you lose! Agent, you win!')
            break
         else:
            while p1 in numberList:
               if (p1 % numberList[j] == 0):
                  del numberList[j]
               else:
                  j += 1
         print(f'\nHere are the remaining numbers: {numberList}')





#=======================================================================
# Don't alter anything below here!

#=======================================================================
# Simple agents always picks first number in list

def agent_smallest(divisors):
   return divisors[0]
   
def agent_random(divisors):

   if len(divisors) == 1:
      return divisors[0]

   else:
      index = random.randrange(len(divisors)-1)
      return divisors[index]
   
#=======================================================================
# Main program:

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
   
   name = input("\nEnter your name:  ")
   agent = input("Which agent do you want to play?  (1) agent_smallest or (2) agent_random:  ")
   turnNum = int(input("Do you want to go (1) first or (2) second?:  "))
   n = int(input("\nEnter positive integer n:  "))

   if agent == "1":
      divisor_game_agent(n, name, turnNum, agent_smallest)
   else:
      divisor_game_agent(n, name, turnNum, agent_random)
   
   playAgain = input("\nDo you want to play again? (y/n):  ")
   

print("\nBye!")


















