

name = "DANG_DUC"
header1 = "CS-335, Spring 2023"
header2 = "A3_HillClimbClique"

import graphs
import random

#=======================================================================
# getRandomset(n, k)
# 
# Inputs: Integers n and k
# Returns:  A list of k random, distinct elements from {0, 1, 2, ..., n-1}
#           (in sorted order)
#=======================================================================
def getRandomSet(n, k):
   tempSet = []
   i=0
   while i < k:
      tempNum = random.randint(0,n-1)
      if tempNum not in tempSet:
         tempSet.append(tempNum)
         i+=1


   tempSet.sort()
   return tempSet

#=======================================================================
# getNumEdges(set, g)
#
# Inputs:  set = a list of distinct vertices
#            g = an undirected graph
#
# Returns:  The number of pairs of adjacent vertices in that list
#=======================================================================
def getNumEdges(set, g):

   count =0
   for x in set:
      for y in set:
         if g[x][y] == 1:
            count+=1

   count = int(count/2)
   return count
#=======================================================================
# getBestNeighbor(n, k, set, g)
#
# Inputs:  n = the number of vertices in graph "g"
#          k = the number of vertices in list "set"
#        set = a list of k distinct vertices
#          g = an undirected graph
#
# Returns:  list [bestNeighbor, numEdges, vertex_eliminated, vertex_added], where:
# 
#           bestNeighbor = a list of k distinct vertices that differs from "set" 
#                          in exactly one vertex and that maximizes the number of edges
#           numEdges     = the number of pairs of adjacent vertices in "bestNeighbor"
#           vertex_eliminated = the vertex removed from "set" to get "bestNeighbor"
#           vertex_added = the vertex added to "set" to get "bestNeighbor"
#
#=======================================================================
def getBestNeighbor(n, k, set, g):

   numEdges = getNumEdges(set,g)
   index  = 0
   vertex = 0
   vertex_e = 0
   vertex_add = 0
   tempSet = set.copy()
   compSet = set.copy()
   while index < k :
         while vertex < n:
            if vertex not in set:
               tempSet[index] = vertex
               tempNum = getNumEdges(tempSet,g)
               if tempNum > numEdges:
                  numEdges = tempNum
                  vertex_add = vertex
                  vertex_e = set[index]
                  set = tempSet.copy()
                  tempSet = compSet.copy()
               else:
                  tempSet=compSet.copy()
            vertex+=1

         vertex = 0
         index+=1


   result = [set,numEdges,vertex_e,vertex_add]
   return result
#=======================================================================
# hillClimbClique(n, k, g, show_steps)
#
# Inputs:  n = the number of vertices in graph "g"
#          k = size of clique we're looking for in graph "g"
#          g = an undirected graph
#          show_steps = a boolean value:  
#                       if true, at each step show vertices eliminated and added, otherwise don't
#
# Returns:  list [finalSet, numEdges], where:
# 
#           finalSet = list of k distinct vertices (in sorted order) for which 
#                      no neighbor increases the number of pairs of adjacent vertices
#           numEdges = number of pairs of adjacent vertices in "finalSet"
#
# Starts with a random set of k vertices and continues finding the best neighbor
# until the best neighbor does not increase the number of adjacent vertices
#
#=======================================================================
def hillClimbClique(n, k, g, show_steps):
  
   set = getRandomSet(n,k)
   numEdges = getNumEdges(set, g)
   index = 0
   vertex = 0
   vertex_e = 0
   vertex_add = 0
   tempSet = set.copy()
   compSet = set.copy()

   print(f'INITIAL SET and NUMBER OF EDGES:\n')
   print(f'{set} \n{numEdges}\n')

   while index < k:
      while vertex < n:
         if vertex not in set:
            tempSet[index] = vertex
            tempNum = getNumEdges(tempSet, g)
            if tempNum >= numEdges:
               numEdges = tempNum
               vertex_add = vertex
               vertex_e = set[index]
               set[index] = vertex
               if show_steps:
                  print(f'\nSubstituted {vertex_e} for {vertex_add}')

               print(f'{set} \n{numEdges}')
            else:
                  tempSet=compSet.copy()
         vertex += 1


      vertex = 0
      index += 1
   print(f'\n')
   set.sort()
   list = [set, numEdges]
   return list
#=======================================================================
#  multipleHillClimbs(n, k, g, show_results, show_steps, repeat):
#
#  This function calls hillClimbClique repeatedly looking for a k-clique in graph g
#  on n vertices until either it finds a k-clique or it has made "repeat" 
#  number of attaempts.
#
#=======================================================================
def multipleHillClimbs(n, k, g, show_results, show_steps, repeat):

   maxNumEdges = -1
   bestSoln = []   
   
   for i in range(repeat):
   
      soln, numEdges = hillClimbClique(n, k, g, show_steps)
      
      if show_results:
         print("RESULT: ")   
         print(soln)
         print(numEdges)
         print()
   
      if numEdges > maxNumEdges:
         bestSoln = soln.copy()
         maxNumEdges = numEdges
            
      if numEdges == k*(k-1)//2:
         break
      
   return [bestSoln, maxNumEdges]
   


#=======================================================================
def testGetRandomSet():
   
   print("\n#=======================================")
   print("testGetRandomSet: \n")
      
   n = 12
   k = 5
   
   for i in range(5):
      print(getRandomSet(n, k))
   print()
      
   n = 100
   k = 10
      
   for i in range(5):
      print(getRandomSet(n, k))
   
   print()
   

#=======================================================================
# DO NOT CHANGE THIS FUNCTION
#=======================================================================
def testGetNumEdges():   

   print("\n#=======================================")
   print("testGetNumEdges: \n")
   
   set = [2, 3, 5, 9, 11]
   numEdges = getNumEdges(set, graphs.graph12)
   print(f'graph12, set = {set}, numEdges = {numEdges}\n')
   
   set = [0, 1, 6, 8, 10]
   numEdges = getNumEdges(set, graphs.graph12)
   print(f'graph12, set = {set}, numEdges = {numEdges}\n')
   
   set = [8, 12, 19, 34, 44, 50, 60, 132, 159, 187]
   numEdges = getNumEdges(set, graphs.graph200)
   print(f'graph200, set = {set}, numEdges = {numEdges}\n')
   
   set = [33, 26, 121, 48, 62, 101, 161, 168, 176, 49]
   numEdges = getNumEdges(set, graphs.graph200)
   print(f'graph200, set = {set}, numEdges = {numEdges}\n')
   
   
#=======================================================================
# DO NOT CHANGE THIS FUNCTION
#=======================================================================
def testGetBestNeighbor():

   print("\n#=======================================")
   print("testGetBestNeighbor: \n")

   set = [0, 1, 6, 8, 10]
   numEdges = getNumEdges(set, graphs.graph12)
   print(f'graph12, set = {set}, numEdges = {numEdges}')

   bestNeighbor, numEdges, x,y = getBestNeighbor(12, 5, set, graphs.graph12)
   print(f'bestNeighbor = {bestNeighbor}, numEdges = {numEdges}\n')


   set = [3, 51, 63, 107, 133, 18, 157, 160, 169, 183]
   numEdges = getNumEdges(set, graphs.graph200)
   print(f'graph200, set = {set}, numEdges = {numEdges}')

   bestNeighbor, numEdges, x,y = getBestNeighbor(200, 10, set, graphs.graph200)
   print(f'bestNeighbor = {bestNeighbor}, numEdges = {numEdges}\n')
   

#=======================================================================
# DO NOT CHANGE THIS FUNCTION
#=======================================================================
def testHillClimbClique():

   print("\n#=======================================")
   print("testHillClimbClique: \n")
   
   print("\n#===================================")
   print("\nGRAPH:  n = 12, k = 5")
   soln, numEdges = hillClimbClique(12, 5, graphs.graph12, True)
   print(f'FINAL:\nSolution = {soln}\n{numEdges}\n')

   
   print("\n#===================================")
   print("\nGRAPH:  n = 12, k = 5")
   soln, numEdges = hillClimbClique(12, 5, graphs.graph12, True)
   print(f'FINAL:\nSolution = {soln}\n{numEdges}\n')

   
   print("\n#===================================")
   print("\nGRAPH:  n = 200, k = 14")
   soln, numEdges = hillClimbClique(200, 14, graphs.graph200, True)
   print(f'FINAL:\nSolution = {soln}\n{numEdges}\n')
   

#=======================================================================
# DO NOT CHANGE THIS FUNCTION
#=======================================================================
def testMultipleHillClimbs(repeat):


   print("\n#=======================================")
   print("testMultipleHillClimbs: \n")


   print("\n#=========================")
   print(f'\nGRAPH:  n = 12, k = 5, repeat = {repeat}\n')
   print("Looking for 10 edges.\n")
   bestSoln, numEdges = multipleHillClimbs(12, 5, graphs.graph12, True, False, repeat)
   print(f'FINAL:  numEdges = {numEdges}, bestSoln = {bestSoln}\n\n')


   print("\n#===================================")
   print(f'\nGRAPH:  n = 200, k = 14, repeat = {repeat}\n')
   print("Looking for 91 edges.\n")
   bestSoln, numEdges = multipleHillClimbs(200, 14, graphs.graph200, True, False, repeat)
   print(f'FINAL:\nbestSoln = {bestSoln}\n{numEdges}\n')
   

   print("\n#====================================")
   print(f'\nGRAPH:  n = 300, k = 22, repeat = {repeat}\n')
   print("Looking for 231 edges.\n")
   bestSoln, numEdges = multipleHillClimbs(300, 22, graphs.graph300, True, False, repeat)
   print(f'FINAL:\nbestSoln = {bestSoln}\n{numEdges}\n')
   

   print("\n#====================================")
   print(f'\nGRAPH:  n = 300, k = 23, repeat = {repeat}\n')
   print("Looking for 253 edges.\n")
   bestSoln, numEdges = multipleHillClimbs(300, 23, graphs.graph300, True, False, repeat)
   print(f'FINAL:\nbestSoln = {bestSoln}\n{numEdges}\n')
   

   print("\n#====================================")
   print(f'\nGRAPH:  n = 300, k = 24, repeat = {repeat}\n')
   print("Looking for 276 edges.\n")
   bestSoln, numEdges = multipleHillClimbs(300, 24, graphs.graph300, True, False, repeat)
   print(f'FINAL:\nbestSoln = {bestSoln}\n{numEdges}\n')

   
   print("\n#====================================")
   print(f'\nGRAPH:  n = 300, k = 25, repeat = {repeat}\n')
   print("Looking for 300 edges.\n")
   bestSoln, numEdges = multipleHillClimbs(300, 25, graphs.graph300, True, False, repeat)
   print(f'FINAL:\nbestSoln = {bestSoln}\n{numEdges}\n')
   
#=======================================================================
   

print(name)
print(header1)
print(header2)
print()

repeat = 30

# UNCOMMENT EACH LINE BELOW ONE AT A TIME TO TEST EACH OF YOUR METHODS


#testGetRandomSet();
#testGetNumEdges();
#testGetBestNeighbor()
#testHillClimbClique()
testMultipleHillClimbs(repeat)

 
