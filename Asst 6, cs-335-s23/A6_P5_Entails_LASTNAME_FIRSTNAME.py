name = "LASTNAME_FIRSTNAME"
header1 = "CS-335, Spring 2023"
header2 = "A6_P5_Entails"

import copy
import A6_data as f


#====== Copy your function here from Problem 3 =========================
def get_resolvents(c1, c2):






      
      


#====== Copy your function here from Problem 4 =========================
def is_satisfiable(clauses, display):  









#===================================================     
def entails(kb, query):  












#====================================================
# DO NOT CHANGE ANYTHING BELOW HERE
#====================================================

def test_entails():

   c = f.entail_check
   n = len(c)//2
   
   print("Entails using Resolution:\n")
   

   for i in range(n):
  
      kb = c[2*i]
      query = c[2*i + 1]
      
      print("=============================================")
      print(f'\nTest #{i+1}\nThe knowledge base: \n')
      for clause in kb:
         print(clause)
      print(f'\nThe query:  {query}\n')
            
      if entails(kb, query):
         print("The knowledge base DOES ENTAIL the query.")
      else:
         print("The knowledge base does NOT entail the query.")
      
   
#=== end test_entails() ================================================   


print()
print(name)
print(header1)
print(header2)
print()

test_entails()
















