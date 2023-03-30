name = 'DANG_DUC'
header1 = 'CS-335, Spring 2023'
header2 = 'A2_P6, A_Star_Seach'


import data as d

# A* shortest path 
# frontier and visited nodes have the form:
#   [location, previous, g_value(location), g_value(location)]

# index constants for nodes:

LOCATION = 0
PREVIOUS = 1
G_VAL = 2
F_VAL = 3

#========================================
def enqueue(pq, new_node):

   i = 0
   while i < len(pq) and new_node[F_VAL] > pq[i][F_VAL]:
      i += 1

   if i == len(pq):
      pq.append(new_node)
   else:
      pq.insert(i, new_node)
      
#========================================
def index_in_visited(visited, location):
   i = 0
   while i < len(visited) and visited[i][LOCATION] != location:
      i += 1
   if i == len(visited):
      return -1
   else:
      return i
#========================================

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

def print_node(node):
   print([names[node[LOCATION]], names[node[PREVIOUS]], node[G_VAL], node[F_VAL]])
      
#========================================
def print_nodelist(nodelist):

   print('[', end = '')
   for node in nodelist:
      print([names[node[LOCATION]], names[node[PREVIOUS]], node[G_VAL], node[F_VAL]], end = ', ')
   print(']')
   
   
####################################################################
def A_Star_Search(graph, h, start, goal, show):

   print(f'start = {names[start]}, goal = {names[goal]}')

   # COMPLETE THIS FUNCTION HERE:
   location = names[start]
   prevLo = names[start]
   gVal = graph[start][start]
   fVal = graph[start][start]+h[start]
   frontier = [[location, prevLo, gVal, fVal] ]

   visited = [[location, prevLo, gVal, fVal] ]

   if show:
      print(f'\nFrontier: {frontier}')
      print(f'Visited: {visited}')

   while(len(frontier)>0):

      frontier = sorted(frontier, key=lambda x: x[3])
      tempNode = frontier.pop(0)
      location = tempNode[0]
      prevLo = tempNode[1]
      gVal = tempNode[2]
      fVal = tempNode[3]

      if show:
            print(f'\n\npopped: {tempNode}')
            print(f'location = {tempNode[0]}, previous = {tempNode[1]}, g_val = {tempNode[2]}, f_val = {tempNode[3]}\n')

      if names.index(location) == goal:

         return tempNode


      for i in range(len(graph[names.index(location)])):
               if isinstance(graph[names.index(location)][i], int) and i!= names.index(location):
                  cost = gVal + graph[names.index(location)][i]
                  fVal = h[i]
                  node = [names[i], location, cost, cost + fVal]
                  if node not in visited and node not in frontier:
                     enqueue(frontier,node)
                     visited.append(node)

      if show:
         print(f'\nFrontier: {frontier}')
         print(f'Visited: {visited}')




   return None










####################################################################


####################################
# DO NOT ALTER ANYTHING BELOW THIS
####################################


print()
print(name)
print(header1)
print(header2)


print('\n###############################################')
print('Graph 0:\n')
print(A_Star_Search(d.graphs[0], d.heuristics[0], 4, 3, True))


print('\n###############################################')
print('Graph 1:\n')
print(A_Star_Search(d.graphs[1], d.heuristics[1], 6, 2, True))




print('\n###############################################')
print('Graph 0:\n')
for i in range(len(d.graphs[0])):
   print(A_Star_Search(d.graphs[0], d.heuristics[0], i, 3, False))
   print()


print('\n###############################################')
print('Graph 1:\n')
for i in range(len(d.graphs[1])):
   print(A_Star_Search(d.graphs[1], d.heuristics[1], i, 2, False))
   print()
   

print('\n###############################################')
print('\nGraph 2:\n')
for i in range(len(d.graphs[2])):
   print(A_Star_Search(d.graphs[2], d.heuristics[2], i, 0, False))
   print()

print('\n###############################################')
print('\nGraph 3:\n')
for i in range(len(d.graphs[3])):
   print(A_Star_Search(d.graphs[3], d.heuristics[3], i, 2, False))
   print()



