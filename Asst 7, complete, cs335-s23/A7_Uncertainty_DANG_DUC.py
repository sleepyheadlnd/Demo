import math

import A7_data as d

name = "DANG_DUC"
header1 = "CS-335, Spring 2023"
header2 = "A7_Uncertainty"

# USE the CONSTANTS below!
# For each literal in your functions that represents one of the below, 
# you will be penalized 1%.

NP = 0  # NP = No Pit
P = 1   # P = Pit
B = 2   # B = Breeze
NB = 3  # NB = No Breeze
U = 4   # U = Unvisited
 

#=======================================================================
# Problem 3:  probConfig(pit_config)
#
# Input:  pit_config = a square 2D array with values P (pit) and NP (no pit)
# 
# Returns:  The probability of the pit configuration, where
#           each cell is assigned a pit with probability 0.2 
#           and that this assignment is independent for each pit.
#
# WRITE THE METHOD:

def probConfig(pit_config):

   prob = 1
   for i in pit_config:
      for j in i:
         if j == P:
            prob *=.2
         else:
            prob*=.8

   return  prob

#=======================================================================
# Problem 4:  nextConfig(pit_config)
#
# Input:  pit_config = a square 2D array with values  P (pit) and NP (no pit)
# 
# Effect:  pit_config is changed to be the next pit configuartion numerically (see assignment)
#
# Returns:  False, if every cell in pit_config has a pit
#           True, otherwise
#
# WRITE THE METHOD:

def nextConfig(pit_config):  

 numRange = int(math.pow (2,len(pit_config)**2)-1)
 sum = int(0)
 e = 0
 for i in pit_config:
    for j in i:
       if j !=0:
         sum+= math.pow(2, e)
       e+=1
 if sum+1 > numRange:
      return False

 sum+=1

 for x in pit_config:
    for y in range(len(x)):
       x[y] = int(sum%2)
       sum /=2
 
 return True

#=======================================================================
# Problem 5:  isConsistent(pit_config, obs)
#
# Input:  pit_config = a square 2D array with values P (pit) and NP (no pit)
#         obs = the observation, a 2D array (same size as pit_config) with values from {B, N, U}, where
#
#           B = BREEZE
#           N = NO BREEZE
#           U = UNVISTED
#
# Returns:  True if the observation is consitent with the pit configuration (see assignment)
#           False, otherwise
#
# WRITE THE METHOD:

def isConsistent(pit_config, obs):

   n = len(pit_config)

   for i in range(n):
       for j in range(n):
           numP = 0
           if pit_config[i][j] == P:
              if ((obs[i][j] == B or obs[i][j] == NB) or
                  (i > 0 and obs[i - 1][j] == NB) or
                  (i < n - 1 and obs[i + 1][j] == NB) or
                  (j > 0 and obs[i][j - 1] == NB) or
                  (j < n - 1 and obs[i][j + 1] == NB)):
                  return False

           if obs[i][j] == B:
              if n == 1 and (pit_config[i][j] == NP or pit_config[i][j] == P):
                  return False
              if i>0 and pit_config[i-1][j] == P:
                  numP+=1
              if i<n-1 and pit_config[i+1][j] == P:
                  numP+=1
              if j > 0 and pit_config[i][j-1] == P:
                  numP+=1
              if j < n-1 and pit_config[i][j+1] == P:
                  numP+=1
              if n>1 and numP == 0:
                  return False

   return True
    
#=======================================================================
# Problem 6:  getProbs(query, obs)
#
# Input: query = a list giving the [row, col] coordinates of the cell for which we want
#                to calculate the probility of a pit, given the observation        
#        obs = the observation, a 2D array (same size as pit_config) with values from {B, N, U}, where
#
#           B = BREEZE
#           N = NO BREEZE
#           U = UNVISTED
#
# Returns:  A list in this format: [round(prob_obs_and_query, 5)
#                                   round(prob_obs, 5),
#                                   round(total_prob, 5)]
#                                   round(conditional_prob, 5)
#
#                 prob_obs_and_query = the probability of both the observation happening
#                                      *and* there being a pit in the queried cell
#
#                 prob_obs = the probability of the observation
#
#                 total_prob = the sum of the probabilites of each configuration
#                              (SUM THEM to help you debug, don't just return 1!)
#
#                 conditional_prob = conditional probability of a pit in the query cell
#                                    given the observatoin

# WRITE THE METHOD:

def getProbs(query, obs):

   prob_obs = 0
   prob_obs_query = 0
   total_prob = 0
   conditional_prob = 1
   n = len(obs)

   #create pit config array
   configArr = [[0 for x in range(n)] for y in range(n)]
   total_prob += probConfig(configArr)

   if isConsistent(configArr, obs):
       probCon = probConfig(configArr)
       prob_obs += probCon
       if configArr[query[0]][query[1]] == P:
           prob_obs_query += probCon

   while nextConfig(configArr):
         probCon = probConfig(configArr)
         total_prob+= probCon

         if isConsistent(configArr,obs):
            prob_obs+= probCon
            if configArr[query[0]][query[1]] == P:
                prob_obs_query+= probCon

   conditional_prob = prob_obs_query / prob_obs

   return [ round(prob_obs_query, 5), 
            round(prob_obs, 5), 
            round(total_prob, 5),
            round(conditional_prob, 5)
          ]

      



#================================================================
# DO NOT ALTER BELOW (for submission)
#================================================================

def test_Problem3_probConfig():

   print("\nTesting Probem 3, probConfig\n")

   for i in range(len(d.query_obs_list)//2):

      config = d.consistency_list[2*i]
      print(f'Test {i}:  {probConfig(config)}')
      
#=========================================================== 

def test_Problem4_nextConfig():

   print("\nTesting Probem 4, nextConfig\n")
  
   config = [[P, P, P], [P, P, P], [P, NP, NP]]
   
   print("config:\n")
   for row in config:
      print(row)
   print()
   
   nextConfig(config)
   
   print("Next config:\n")
   
   for row in config:
      print(row)
   print()


   print("Start config:\n")
   config = [[NP, NP], [NP, NP]]
   
   for row in config:
      print(row)
   print()
  
  
   while nextConfig(config):
      print("next config:\n")
      for row in config:
         print(row)
      print()
   
   

#================================================================
  


def test_Probem5_isConsistent():

   print("\nTesting Probem 5, isConsistent\n")
   for i in range(len(d.consistency_list)//2):
      pit_config = d.consistency_list[2*i]
      obs = d.consistency_list[2*i + 1]
      print(f'Test {i}:  {isConsistent(pit_config, obs)}')

#================================================================

def test_Problem6_getProbs():

   print("\nTesting Probem 6 HELP, getProbs\n")
   for i in range(len(d.query_obs_list)//2):
   
      query = d.query_obs_list[2*i]
      obs = d.query_obs_list[2*i + 1]
      probs = getProbs(query, obs)
      
      print(f'Test {i}:  {probs}')

   
#================================================================




print()
print(name)
print(header1)
print(header2)

print("\n=============================================")

#test_Problem3_probConfig()
#test_Problem4_nextConfig()
#test_Probem5_isConsistent()
test_Problem6_getProbs()

