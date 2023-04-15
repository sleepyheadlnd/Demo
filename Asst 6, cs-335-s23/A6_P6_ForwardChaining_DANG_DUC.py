name = "DANG_DUC"
header1 = "CS-335, Spring 2023"
header2 = "A6_P6_Forward_Chaining"


import copy
import A6_data as f


#====================================================
def forward_chaining(kb, query, display = False):

   queueL = []
   dequeueL =[]
   i=0
   while i < len(kb):
      if len(kb[i])== 1:
         queueL+= kb[i]
         kb[i].pop(0)
         i-=1
      i+=1

   while len(queueL)!=0 :
          deq = queueL.pop(0)
          dequeueL.append(deq)
          for j in kb   :
              if deq in j[0:-1]:
                 j.remove(deq)
              if '~'+deq in j[0:-1]:
                 j.remove('~'+deq)
              if len(j)==1:
                 if j[0] not in dequeueL:
                  queueL+=j
                 j.remove(j[0])
   if(display):
      print(f'inferred = {dequeueL}\n')
      for i in range(len(kb)):
         print(f'clause {i}: count = {len(kb[i][:-1])}')

   if query in dequeueL:
      return True
   return False
   
   
   

#====================================================
# DO NOT CHANGE ANYTHING BELOW HERE
#====================================================

def test_forward_chaining():

   c = f.forward_chaining_check
   n = len(c)//2
   
   print("Entails using Forward Chaining:")

   for i in range(n):
  
      kb = c[2*i]
      query = c[2*i + 1]
      
      print("\n=================================================")
      print(f'Test #{i+1}')

      print('\nThe knowledge base: \n')
      for clause in kb:
         print(clause)
      print(f'\nThe query: {query}\n')
            
      if forward_chaining(kb, query, False):
         print(f'The knowledge base DOES ENTAIL query {query}.')
      else:
         print(f'The knowledge base does NOT entail query {query}.')
      
#=== end test_forward_chaining() ================================================   


            

print()
print(name)
print(header1)
print(header2)
print()

test_forward_chaining()























