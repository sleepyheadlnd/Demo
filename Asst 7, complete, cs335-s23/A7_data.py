# A8_data

NP = 0  # NP = No Pit
P = 1   # P = Pit
B = 2   # B = Breeze
NB = 3  # NB = No Breeze
U = 4   # U = Unvisited


   
query_obs_list = [

# 0
      [0, 1],
      [ 
         [NB,  U],
         [ U,  U],
      ],


# 1
   [1, 1],
      [ 
         [NB,  B],
         [ U,  U],
      ],

      
# 2      
      [0, 2],
      [ 
         [NB, NB,  U],
         [ B,  U, NB],
         [ U,  U,  U],
      ],
   


# 3
      [0, 2],
      [ 
         [NB,  B,  U],
         [ B,  U,  U],
         [ U,  U,  U],
      ],
    

# 4
      [0, 2],
      [ 
         [NB,  B,  U,  U],
         [ B,  U,  U,  U],
         [ U,  U,  U,  U],
         [ U,  U,  U,  U],
      ],
   


# 5
      [2, 2],
      [ 
         [ U, NB,  U,  U],
         [ U,  U,  B,  B],
         [ B,  U,  U,  U],
         [ U,  B,  U, NB],
      ],
   
   

# 6
      [0, 2],
      [ 
         [NB,  B,  U,  U],
         [NB,  U,  U,  U],
         [ U,  U,  U,  U],
         [ U,  U,  U,  U],
      ],
      
      
   
# 7
      [1, 3],
      [ 
         [NB,  B,  U,  U],
         [NB,  U,  U, NB],
         [ U,  U,  B,  U],
         [ U,  U,  U,  U],
      ],
      
      
# 8
      [1, 1],
      [ 
         [NB,  B,  U,  U],
         [ B,  U,  U,  U],
         [ U,  U,  U,  U],
         [ U,  U,  U,  U],
      ],
      

# 9
      [3, 3],
      [ 
         [ U,  U,  U,  U],
         [ U,  U,  U, NB],
         [ U,  U, NB,  U],
         [ U, NB,  B,  U],
      ],
   

# 10   
      [3, 1],
      [ 
         [ U,  U,  U,  U],
         [ U,  U,  U,  U],
         [ U,  U,  U,  U],
         [ U,  U,  U,  U],
      ],


# 11
      [1, 2],
      [ 
         [ U, NB,  U,  U],
         [ U,  U,  U,  B],
         [ B,  U,  B,  U],
         [ U,  U,  U,  U],
      ],


# 12
      [3, 2],
      [ 
         [ U, NB,  U,  U],
         [ U,  U,  U,  B],
         [ B,  U,  B,  U],
         [ U,  B,  U,  U],
      ],

   
] #======= end query_obs_list =========================


      
consistency_list = [

# 0
      [
         [P],
      ],
      [
         [U],
      ],
     
# 1     
      [
         [P],
      ],
      [
         [B],
      ],
      
# 2     
      [
         [P],
      ],
      [
         [NB],
      ],
     
# 3
      [
         [NP],
      ],
      [
         [B],
      ],

# 4
      [
         [NP, NP, NP],
         [NP, NP,  P],
         [ P,  P, NP],
      ],
      [ 
         [NB,  B,  U],
         [ B,  U,  U],
         [ U,  U,  U],
      ],

# 5
      [
         [NP, NP, NP],
         [NP,  P,  P],
         [NP, NP, NP],
      ],
      [ 
         [NB,  B,  U],
         [ B,  U,  U],
         [ U,  U,  U],
      ],

# 6
      [
         [NP, NP, NP],
         [NP,  P,  P],
         [NP, NP, NP],
      ],
      [ 
         [NB,  B,  U],
         [ B,  U,  U],
         [ U,  U,  U],
      ],

# 7
      [
         [NP, NP,  P],
         [NP, NP,  P],
         [ P,  P, NP],
      ],
      [ 
         [NB,  B,  U],
         [ B,  U,  U],
         [ U,  U,  U],
      ],
      
# 8      
      [
         [NP,  P,  P],
         [NP, NP,  P],
         [ P,  P, NP],
      ],
      [ 
         [NB,  B,  U],
         [ B,  U, NB],
         [ U, NB, NP],
      ],
      
# 9
      [
         [NP, NP, NP],
         [NP,  P, NP],
         [NP, NP, NP],
      ],
      [ 
         [ B, NB,  B],
         [NB,  U, NB],
         [ B, NB,  B],
      ],
      
# 10      
      [
         [NP, NP, NP],
         [NP,  P, NP],
         [NP, NP, NP],
      ],
      [ 
         [NB, NB, NB],
         [NB,  B, NB],
         [NB, NB, NB],
      ],
      
# 11      
      [
         [NP, NP, NP],
         [NP,  P, NP],
         [NP, NP, NP],
      ],
      [ 
         [NB, NB, NB],
         [NB,  U, NB],
         [NB, NB,  B],
      ],
      
# 12      
      [
         [NP, NP, NP],
         [NP,  P, NP],
         [NP, NP, NP],
      ],
      [ 
         [NB, NB, NB],
         [NB,  U, NB],
         [NB,  B, NB],
      ],
      

# 13      
      [
         [NP, NP, NP],
         [NP, NP,  P],
         [ P, NP, NP],
      ],
      [ 
         [NB,  B, NB],
         [ B, NB,  U],
         [NB, NB, NB],
      ],

# 14      
      [
         [NP,  P, NP],
         [NP, NP,  P],
         [ P, NP, NP],
      ],
      [ 
         [ B,  U,  B],
         [NB,  U,  U],
         [ U,  B,  B],
      ],
      


] #======= end consistency_list =========================      
      



