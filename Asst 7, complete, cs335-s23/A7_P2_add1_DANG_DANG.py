import math

name = "DANG_DANG"
header1 = "CS-335, Spring 2023"
header2 = "A7_P2_add1"


# WRITE THE METHOD:

def add1(array):

   numRange = math.pow(2,len(array))-1
   j=0
   sum = int(0)

   for i in range(len(array)):
      if array[i] != 0:
         sum+= math.pow(2, i)
      i-=1

   if sum+1 > numRange:
      return False

   sum+=1

   while sum >= 1:
         array[j]=int(sum % 2)
         sum /=2
         j+=1

   return True


#================================================================
# DO NOT ALTER BELOW (for submission)
#================================================================
    
    
    
print()
print(name)
print(header1)
print(header2)

print("\n=============================================")

def display(x):
   y = x.copy()
   y.reverse()
   print(y)

keepGoing = True

x = [0, 0, 0, 0, 0]

while keepGoing:
   display(x)
   keepGoing = add1(x)




