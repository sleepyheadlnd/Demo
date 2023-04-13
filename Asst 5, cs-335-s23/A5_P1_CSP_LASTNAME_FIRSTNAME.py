name = "LASTNAME_FIRSTNAME"
header1 = "CS-335, Spring 2023"
header2 = "A5_P1_CSP"

import copy  # for deepcopy
import graphs_A5_P1 as input


#=======================================================================
# getDomains:
#
# Input:  n = number of vertices
#         m = number of colors.
#
# Returns:  domains =  the initial list of possible colors for each vertex, i.e.,
#                      domains[i] = [1, 2, 3, ..., m] for 0 <= i <= n-1.

def getDomains(n, m):
   colors = [i for i in range(1, m+1)]
   domains = []
   for i in range(n):
      domains.append(colors.copy())
   return domains


#=======================================================================
# Problem 1a
#
# getDegrees:
#
# Input: undirected and unweighted graph g.
#
# Returns:  degrees = a list of the degrees of the vertices in g.
#                        I.e., degrees[i] = the degree of vertex i.
#
# WRITE THIS METHOD:

def getDegrees(g):
  return





#=======================================================================
# backtrackingSearch:
#
# Input:  g = the graph
#         m = number of colors
# 
# Sets up domains and degrees, and makes initial call to "backtrack"
#
# Returns:  An m-coloring (list of domains each with one color), if one exists, or
#           The empty list (if no m-coloring exists).

def backtrackingSearch(g, m):

   domains = getDomains(len(g), m)
   degrees = getDegrees(g)
   return backtrack(g, domains, degrees)
   

#=======================================================================
# Problem 1b
#
# getNextVariable:
#
# Inputs:  g = an undirected, unweighted graph.
#          domains = list of remaining colors for each vertex
#          degrees = list of degrees of each vertex
#
# Returns: the variable index with the Minimum Remaining Values (not including
#    those with only 1 remaining value), with ties broken by highest degree. If 
#    there are ties beyond that, the smallest indexed vertex is picked.
#
#    If no variable has more than 1 remaining value, returns -1.
#
# WRITE THIS METHOD:

def getNextVariable(g, domains, degrees):
   return




   

#=======================================================================
# Problem 1c
#
# AC3:
#
# Input:  g = the graph
#         domains = list of remaining colors for each vertex
#         v = vertex whose domain has just been changed
#
# Returns:  The list of pruned domains resulting from the AC3 pruning algorithm,
#           but if any domains becomes empty, AC3 returns an empty list.
#
# WRITE THIS METHOD:

def AC3(g, domains, v):
   return





      
#=======================================================================
# Problem 1d
# 
# backtrack
#
# Input:  g = the graph
#         domains = list of possible colors for each vertex
#         degrees = list of degrees of each vertex
# 
# Performs recursive backtracking using MRV then degree for variable selection
#    and AC3 forward checking for inference
#
# Returns:  An m-coloring within initial domains, if one exists, or
#           The empty list (if no such m-coloring exists).
#
# WRITE THIS METHOD:

def backtrack(g, domains, degrees):
   return



           
           
#=================================================
# test getDegrees(g)

def test_getDegrees():

   print("\n=============================================")
   print(name)
   print("TESTING:  getDegrees(g)")

   for i in range(len(input.graphs)):
      g = input.graphs[i]
      print(f'\ni = {i}, n = {len(g)}:')
      print(getDegrees(g))

#=================================================
# test getNextVariable(g, domains, degrees):

def test_getNextVariable():

   print("\n\n=============================================")
   print(name)
   print("TESTING:  getNextVariable(g, domains, degrees)\n")

   g = input.graphs[0]
   degrees = [1, 2, 1]
   domains = [[1, 2], [1, 2], [1, 2]]
   print(f'Next Variable:  {getNextVariable(g, domains, degrees)}')

   g = input.graphs[0]
   degrees = [1, 2, 1]
   domains = [[2], [1], [2]]
   print(f'Next Variable:  {getNextVariable(g, domains, degrees)}')

   g = input.graphs[1]
   degrees = [2, 3, 3, 3, 2, 3]
   domains = [[1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
   print(f'Next Variable:  {getNextVariable(g, domains, degrees)}')


   g = input.graphs[3]
   degrees = [4, 3, 4, 4, 3, 3, 4, 4, 2, 3, 4]
   domains = [[1], [1, 2, 3], [2], [1, 2, 3], [2, 3], [1, 3], [1, 2, 3], [1, 3], [2, 3], [1, 3], [2, 3]]
   print(f'Next Variable:  {getNextVariable(g, domains, degrees)}')

   g = input.graphs[4]
   degrees = [4, 3, 4, 4, 3, 3, 5, 4, 3, 3, 4]
   domains = [[1, 3, 4], [2], [2], [2, 3, 4], [2, 3, 4], [3, 4], [1], [1], [2, 3, 4], [3, 4], [1, 3, 4]]
   print(f'Next Variable:  {getNextVariable(g, domains, degrees)}')

   g = input.graphs[5]
   degrees = [10, 10, 10, 10, 11, 10, 10, 9, 9, 10, 10, 11, 10, 11, 11, 10, 11, 11, 11, 11, 11, 11, 11, 12, 11, 11, 10, 11, 11, 11, 12, 10, 11, 10, 10, 11, 10, 12, 12, 12]
   domains = [[4], [4, 5, 6], [3, 4, 5, 6], [2, 3, 4, 6], [2], [2, 3, 4, 6], [4], [2], [4], [4], [2, 5, 6], [1], [1], [1], [4], [2, 4, 6], [2], [2], [3], [3], [5], [1], [3, 5, 6], [1], [2], [3], [2], [1], [3], [1], [3], [5], [1], [6], [4, 5, 6], [5], [1, 4, 5, 6], [2], [1], [1]]
   print(f'Next Variable:  {getNextVariable(g, domains, degrees)}')




#=================================================
# test AC3(g, domains, v)

def test_AC3_helper(g, domains, v):

   print(f'\ninitial size = {sum([len(d) for d in domains])}' )
   print(f'domains:  {domains}')
   AC3_result = AC3(g, domains, v)
   print(f'AC3 Result:  {AC3_result}')
   print(f'result size = {sum([len(d) for d in AC3_result])}' )


def test_AC3():

   print("\n\n=============================================")
   print(name)
   print("TESTING:  AC3(g, domains, v)")

   
   g = input.graphs[0]
   domains = [[1, 2], [1], [1, 2]]
   v = 1
   test_AC3_helper(g, domains, v)

   g = input.graphs[1]
   domains = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1]]
   v = 5
   test_AC3_helper(g, domains, v)

   g = input.graphs[1]
   domains = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1]]
   v = 5
   test_AC3_helper(g, domains, v)

   g = input.graphs[3]
   domains = [[1], [2, 3], [2], [2], [2, 3], [1, 3], [1, 2, 3], [1], [2, 3], [1, 3], [2, 3]]
   v = 3
   test_AC3_helper(g, domains, v)

   
   g = input.graphs[6]
   domains = [[2], [1, 3], [1, 2, 3], [3], [1, 2], [1, 2, 3], [2, 3], [1, 2], [2], [1, 2], [1], [3], [2], [1, 3], [2, 3], [1, 3], [1, 2, 3], [2, 3], [2], [1, 2, 3], [1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 3], [2, 3], [1, 3], [1], [1, 2, 3], [1, 3]]   
   v = 0
   test_AC3_helper(g, domains, v)

   
   g = input.graphs[10]
   domains = [[1, 3, 5, 6], [1, 2, 3, 5], [1, 3, 5], [2, 3, 5, 6], [2, 3, 5], [1, 2, 3, 5, 6], [3, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5], [1, 3, 5], [1, 2, 3, 4, 5], [1, 2, 3, 5], [1, 3, 4, 5], [1, 3, 4, 5, 6], [3, 4, 5], [1, 2, 3, 5], [3, 4, 5, 6], [3, 4, 5], [3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [3], [1, 3, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5], [1, 3, 4, 5, 6], [1, 3, 4, 5, 6], [3, 5], [2, 3, 5, 6], [1, 2, 3, 4, 5, 6], [3, 5], [1, 3, 5], [2, 3, 4, 5], [2, 3, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 6], [2, 3, 5, 6], [3, 5], [1], [3, 5], [2, 3, 4, 5, 6], [2, 3, 5, 6], [4], [1, 2, 3, 4, 5], [3, 5, 6], [2, 3, 4, 5], [3, 5], [1, 2, 3, 5], [2, 3, 5, 6], [3, 4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [2, 3, 5, 6], [2], [1, 3, 4, 5, 6], [6], [3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [3, 4, 5, 6], [3, 5], [3, 5], [2, 3, 4, 5], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6]]
   v = 26
   test_AC3_helper(g, domains, v)



#=================================================
# test backtrackingSearch(g, m)

def test_backtrackingSearch():

   print("\n\n=============================================")
   print(name)
   print("TESTING:  backtrackingSearch(g, m)\n")

   for i in range(len(input.graphs)):
      
      g = input.graphs[i]
      print(f'\nTest {i}, n = {len(g)}:\n')
      
      m = 2
      keep_going = True
      
      ans = []
      while keep_going:
         print(f'm = {m}')
         ans = backtrackingSearch(g, m)
         if ans == []:
            m += 1
         else:
            keep_going = False
      
      print(f'Graph[{i}] requires {m} colors:\n')
      print(ans)
      print("-----------------------------------")
  
      
#=================================================
# main program

#test_getDegrees()
#test_getNextVariable()
#test_AC3()
#test_backtrackingSearch()







