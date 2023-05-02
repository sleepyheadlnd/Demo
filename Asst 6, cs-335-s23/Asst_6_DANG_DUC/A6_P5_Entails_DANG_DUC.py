name = "DANG_DUC"
header1 = "CS-335, Spring 2023"
header2 = "A6_P5_Entails"

import copy
import A6_data as f


#====== Copy your function here from Problem 3 =========================
def get_resolvents(c1, c2):

   res = []
   temp = []

   for i in c1:
      for j in c2:
         if i == '~' + j or j == '~' + i:
            for x in c1:
               if x != i and x not in temp:
                  temp.append(x)
            for y in c2:
               if y != j and y not in temp:
                  temp.append(y)
            temp.sort()
            res.append(temp)
            temp = []
   return res

#====== Copy your function here from Problem 4 =========================
def is_satisfiable(clauses, display):
   all = []
   all += clauses
   round = 1
   l=0
   # for list in clauses:
   #    all.append(list)
   while (l < len(all)):
      l = len(all)
      pair = 1
      if (display):
         print(f'len(all) = {l}:\n')
         for li in range(l):
            print(f'all[{li}] = {all[li]}')
         print(f'\n======================= round {round} =========================\n')
      for i in range(len(clauses)):
         j = i + 1
         while j < len(clauses):
            new_resovent = get_resolvents(clauses[i], clauses[j])
            if (display):
               print(f'pair number {pair}:')
               print(f'all[{i}] = {clauses[i]}')
               print(f'all[{j}] = {clauses[j]}')
               print(f'resolvent = {new_resovent}\n')
               pair += 1
            # new_resovent.sort()
            if new_resovent == [[]]:
               return False
            for x in new_resovent:
               if x not in all:
                  all.append(x)
            j += 1

      # if l == len(all):
      #    return True
      # if (display):
      #    print('\n======================')
      clauses = []
      clauses += all
      round += 1
      # for list in all:
      #    clauses.append(list)

   return True

#===================================================     
def entails(kb, query):

   if query[0] == '~':
      kb.append(query[1:])
   else:
      kb.append(['~'+query])

   if(is_satisfiable(kb,False)):
      return False

   return True

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
















