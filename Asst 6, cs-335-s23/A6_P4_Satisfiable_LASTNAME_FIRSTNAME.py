name = "LASTNAME_FIRSTNAME"
header1 = "CS-335, Spring 2023"
header2 = "A6_P4_Satisfiable"

import copy
import A6_data as f


#====== Copy your function here from Problem 3 =========================
def get_resolvents(c1, c2):






      
      


#=======================================================================     
def is_satisfiable(clauses, display):  









#====================================================
# DO NOT CHANGE ANYTHING BELOW HERE
#====================================================

def test_sat():

   formulas = f.sat_check
      
   F4 = formulas[4]
   print(f'\nformula F4:  {F4}\n')
   ans = is_satisfiable(F4, True)
   if ans:
      print('This formula IS SATISFIABLE.\n')
   else:
      print('This formula is NOT satisfiable.\n')
      
   print(f'\n============================================\n\n')
   print()


   F3 = formulas[3]
   print(f'formula F3:  {F3}')
   ans = is_satisfiable(F3, True)
   if ans:
      print('This formula IS SATISFIABLE.\n')
   else:
      print('This formula is NOT satisfiable.\n')
   
   print(f'\n============================================\n\n')
   print()


   for i in range(len(formulas)):
      print(f'formulas[{i}]:  {formulas[i]}')
      ans = is_satisfiable(formulas[i], False)
      if ans:
         print('This formula IS SATISFIABLE.\n')
      else:
         print('This formula is NOT satisfiable.\n')
     

#=== end test_sat() ================================================     


print()
print(name)
print(header1)
print(header2)
print()

test_sat()


