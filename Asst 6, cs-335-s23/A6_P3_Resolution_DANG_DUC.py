name = "LASTNAME_FIRSTNAME"
header1 = "CS-335, Spring 2023"
header2 = "A6_P3_Resolution"

import copy
import A6_data as f


#====================================================
def get_resolvents(c1, c2):

   res = []
   temp = []

   for i in c1:
      for j in c2:
         if i == '~'+j or j == '~'+i :
            for x in c1:
               if x != i:
                  temp.append(x)
            for y in c2:
               if y != j:
                  temp.append(y)
            res.append(temp)
            temp=[]
   return res


#====================================================
# DO NOT CHANGE ANYTHING BELOW HERE
#====================================================
def test_get_resolvents():

   c = f.resolve_check
   n = len(c)//2

   for i in range(n):
   
      j = 2*i
      k = 2*i + 1
      print(f'\nc[{j}] = {c[j]}')
      print(f'c[{k}] = {c[k]}\n')
      print("resolvents:\n")
      rs = get_resolvents(c[j], c[k])
      if rs == []:
         print("No resolvents!")
      else: 
         for clause in rs:
            print(clause)
      print()


#=== end test_get_resolvents() ==================================================   


print()
print(name)
print(header1)
print(header2)
print()
     
test_get_resolvents()    


