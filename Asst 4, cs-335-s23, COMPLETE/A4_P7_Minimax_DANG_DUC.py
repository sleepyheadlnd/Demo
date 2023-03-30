import math  # use math.inf and -math.inf for infinity and negative infinity

name = "DANG_DUC"
header1 = "CS-335, Spring 2023"
header2 = "A4_P7_Minimax"


#=======================================================================
# COPY YOUR FUNCTION "divisor_game_agent(n, name, turnNum, agent)" here:
#

def divisor_game_agent(n, name, turnNum, agent):
   numberList = []
   for i in range(1, n + 1):
      if (n % i == 0):
         numberList.append(i)

   print(f'\nHere are the remaining numbers: {numberList}')

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

         D = agent(numberList)
         p2 = D[1]
         print(f'Agent picked {p2}.  (Agent visited {D[2]+1} nodes to determine this.)')
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
         L = agent(numberList)
         p2 = L[1]
         print(f'Agent picked {p2}.  (Agent visited {L[2]+1} nodes to determine this.)')
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
# DG_Max_Value:
#
# Input: divsors, a list of the remaining divisors.
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the maximum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves maximum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Max_Value(divisors):

   temp = divisors.copy()
   max_u = -math.inf
   j = 0
   count =0
   if len(divisors) == 0:

      return [1,0,0]

   for x in divisors:
      y = x
      while y in temp:
         if (y % temp[j] == 0):
            del temp[j]
         else:
            j += 1
      count+=1
      min_S = DG_Min_Value(temp)
      temp_u = min_S[0]
      count+= min_S[2]
      if temp_u > max_u:
         max_u = temp_u
         best_a = x
      j=0
      temp = divisors.copy()

   min_L = [max_u,best_a,count]
   return min_L




#=======================================================================
# DG_Min_Value:
#
# Input: divsors, a list of the remaining divisors.
#
# Returns a list:  [u, a, numNodes]
#
#    where u = the minimum utility that can be achieved at this node (divisors)
#          a = the action (divisor to pick) that achieves minimum utility
#          numNodes = number of nodes examined (including the current node) to determine this

def DG_Min_Value(divisors):

   temp = divisors.copy()
   min_u = math.inf
   j = 0
   count = 0
   if len(divisors) == 0:
      return [0,0,0]

   for x in divisors:
      y = x
      while y in temp:
         if (y % temp[j] == 0):
            del temp[j]
         else:
            j += 1
      count+=1
      max_S = DG_Max_Value(temp)
      temp_u = max_S[0]
      count+=max_S[2]
      if temp_u < min_u:
         min_u = temp_u
         best_a = x
      j=0
      temp = divisors.copy()

   max_L = [min_u, best_a, count]
   return max_L






#=======================================================================
# Don't alter anything below here!

print()
print(name)
print(header1)
print(header2)
print()

print("Welcome to the Divisor Game, version MINIMAX!")
name = input("\nEnter your name:  ")

playAgain = 'y'
testNum = 0

while playAgain[0] in ['y', 'Y']:

   print("\n=========================================================")
   testNum += 1
   print(f'Test case {testNum}:')
   
   turnNum = int(input("\nDo you want to go (1) first or (2) second?:  "))
   n = int(input("\nEnter positive integer n:  "))

   divisor_game_agent(n, name, turnNum, DG_Min_Value)

   playAgain = input("\nDo you want to play again? (y/n):  ")
   print()

print("\nBye!")
