name = 'DUC_DANG'
header1 = 'CS-335, Spring 2023'
header2 = 'A2_P5_JUGS_BFS'


# index constants for nodes in visited:
CURRENT = 0
PREVIOUS = 1

#========================================
def index_in_visited(visited, amounts):
   i = 0
   while i < len(visited) and visited[i][CURRENT] != amounts:
      i += 1
   if i == len(visited):
      return -1
   else:
      return i

#=======================================
# def process_amounts(next, frontier, visited):
#
#    index = index_in_visited(visited, next)
#    if index == -1:
#       visited.append([next, amounts])
#       frontier.append(next)
#

#=======================================
def Jugs_BFS(caps, show):

   # caps = [capacity of Jug A, capacity of Jug B, capacity of Jug C]
   # Given:  capacity of Jug A is even.
   # Jug A starts full, others empty
   # Goal: Get half of water in A into B and half into A, with C empty
   
   # parameter "show" is a Boolean.
   # If it is True, then at each step, show the frontier and visited lists, and the amounts that are popped
   
   # Return:  [path, visited], where path is the shortest path from the start to the goal state,
   #  and visited is the visited array.
   #  If there is no way to reach the goal state, return an empty list for the path.
   
   # Write this method:
   frontier = [[caps[0],0,0]]
   visited = [[caps[0],0,0],[caps[0],0,0]]
   goal = caps[0] / 2
   visitLen = 0
   capA, capB, capC = caps[0], caps[1], caps[2]

   while(len(frontier)>0):
      if show:
         print(f'frontier =  {frontier}')
         print(f'visisted = {visited}')
      popA = frontier.pop(0)
      a, b, c = popA[0], popA[1], popA[2]
      tempNode = []

      if show:
         print(f'\npopped amount = {popA}\n\n')

      if a == goal and b == goal:
         path = []
         del visited[-1]
         while popA != [caps[0],0,0]:
            path.append(popA)
            index = index_in_visited(visited, popA)
            popA = visited[index][1]
         path.append(popA)
         path.reverse()
         return [path, visited]


      #A to B and A to C
      if a != 0:
         # A to B
         if a + b >= capB:
            amountB = capB
            amountA = a - (capB - b)
            state = [amountA, amountB,c]
         if a + b <= capB:
            amountB = a + b
            amountA = 0
            state = [amountA, amountB, c]
         tempNode.append(state)
         # A to C
         if a + c >= capC:
            amountC = capC
            amountA = a - (capC - c)
            state = [amountA, b,amountC]
         if a + c <= capC:
            amountC = a + c
            amountA = 0
            state = [amountA, b, amountC]
         tempNode.append(state)

      # B to A and B to C
      if b != 0:
         # B to A
         if a + b >= capA:
            amountA = capA
            amountB = b - (capA - a)
            state = [amountA, amountB,c]
         if a + b <= capA:
            amountA = a + b
            amountB = 0
            state = [amountA, amountB, c]
         tempNode.append(state)
         # B to C
         if c + b >= capC:
            amountC = capC
            amountB = b - (capC - c)
            state = [popA[0], amountB,amountC]
         if b + c <= capC:
            amountC = b + c
            amountB = 0
            state = [a, amountB, amountC]
         tempNode.append(state)

         # C to A and C to B
      if c != 0:
            # C to A
            if a + c >= capA:
               amountA = capA
               amountC = c - (capA - a)
               state = [amountA, b, amountC]
            if a + c <= capA:
               amountA = a + c
               amountC = 0
               state = [amountA, b, amountC]
            tempNode.append(state)
            # C to B
            if b + c >= capB:
               amountB = capB
               amountC = c - (capB - b)
               state = [a, amountB, amountC]
            if c + b <= capB:
               amountB = c + b
               amountC = 0
               state = [a, amountB, amountC]
            tempNode.append(state)
      for node in tempNode:
             if index_in_visited(visited,node) == -1 and node not in visited:
                frontier.append(node)
                visited.append([node,popA])





   # Return empty list if goal state is not reached
   return []









                  
####################################
# DO NOT ALTER ANYTHING BELOW THIS
####################################


def test(caps, show):
   
   print(f'\n###########################################################')
   print(f'Jug capacities:  {caps}\n')
   
   result = Jugs_BFS(caps, show)
   
   if result == []:
      print('Not possible')
   else:
      path, visited = result
      print(f'Best solution:  {path}')
      print(f'Number of pours:  {len(path) - 1}')
      print(f'Visited length:  {len(visited)}')
      
      

print()
print(name)
print(header1)
print(header2)


test([6, 4, 1], True)
test([6, 4, 1], False)

test([8, 5, 3], True)
test([8, 5, 3], False)

test([10, 7, 4], False)

test([12, 9, 7], False)

print('\n=========== END OF INITIAL TESTS ==============================================\n')


test([10, 6, 2], False)

test([10, 7, 3], False)

test([16, 9, 7], False)

test([20, 12, 1], False)

test([32, 17, 15], False)

test([60, 51, 17], False)







