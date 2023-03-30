name = 'DANG_DUC'
header1 = 'CS-335, Spring 2023'
header2 = 'A2P1, Rumba Simulation'


import random

# Environment:  [room_num, room 1 status, room 2 status]
# Percept:  [room_num, room_status]


NUM_DAYS = 40

STAY = 'STAY'
VACUUM = 'VACUUM'
RIGHT = 'RIGHT'
LEFT = 'LEFT'
DIRTY = 'DIRTY'
CLEAN = 'CLEAN'

ROOM_NUM = 0 # index into percept and environment to get Room #
STATUS = 1  # index into percept to get status (dirty or clean)


def get_dirt(p):
   return random.random() < p


###############################################################
class Agent:

   def __init__(self, name, p, vacP, moveP, oneP, twoP):
   
      self.name = name
      self.p = p
      self.vacP = vacP
      self.moveP = moveP
      self.oneP = oneP
      self.twoP = twoP
      
   perceptHistory = []
   
   def getName(self):
      return name
   
   def getAction(self, percept):
      
      self.perceptHistory.append(percept)
      
      curr = self.perceptHistory[-1]
      if curr[STATUS] == DIRTY:
         return VACUUM
      elif curr[ROOM_NUM] == 1:
         return RIGHT
      elif curr[ROOM_NUM] == 2:
         return LEFT
         
#### End Class Agent #############################################
   

#### rumba_simulate ##############################################
def rumba_simulation(f, agent, p, vacP, moveP, oneP, twoP):

   score = 0
   
   f.write(f'Agent: {agent.getName()}\n\n') 
   f.write(f'probability of dirt:  {p}\n')
   f.write(f'points for moving:  {moveP}\n')
   f.write(f'points for vacuuming:  {vacP}\n')
   f.write(f'points for exactly one room clean:  {oneP}\n')
   f.write(f'points for exactly two rooms clean:  {twoP}\n\n\n')
   
   # COMPLETE THIS FUNCTION HERE:
   status = [[],CLEAN,CLEAN]
   roomNumb=1
   percept =[roomNumb,status[roomNumb]]
   f.write(f'Morning #{0}:\n')
   f.write(f'Environment: {[roomNumb, status[1], status[2]]}\n')
   f.write(f'Percept: {percept}\n')
   f.write(f'Score: {score}\n\n')
   action = agent.getAction(percept)
   f.write(f'Night action = {action}\n\n')

   for i in range(1, NUM_DAYS):

      if action == RIGHT:
         roomNumb = 2
         score += moveP
      elif action == LEFT:
         roomNumb = 1
         score += moveP
      elif action == VACUUM:
         status[roomNumb]=CLEAN
         score += vacP

      for x in range(1, 3):
         if get_dirt(p) == True:
            status[x] = DIRTY

      percept = [roomNumb, status[roomNumb]]
      f.write(f'Morning #{i}:\n')
      f.write(f'Environment: {[roomNumb, status[1], status[2]]}\n')

      if (status[1] == CLEAN and status[2] == DIRTY) | (status[2] == CLEAN and status[1]==DIRTY):
         score += oneP
      else:
         score += twoP

      f.write(f'Percept: {percept}\n')
      f.write(f'Score: {round(score,2)}\n\n')

      action = agent.getAction(percept)
      f.write(f'Night action = {action}\n\n')
   ################# end for loop############
   if (action == RIGHT):
      roomNumb = 2
      score += moveP
   elif (action == LEFT):
      roomNumb = 1
      score += moveP
   else:
      status[roomNumb] = CLEAN
      score += vacP

   f.write(f'Morning #{NUM_DAYS}:\n')
   f.write(f'Environment: {[roomNumb, status[1], status[2]]}\n\n')
   f.write(f'FINAL SCORE: {round(score,2)}\n')
   f.write(f'##########################################################\n\n')

   return score
      
#### end rumba_simulate #########################################




####################################
# DO NOT ALTER ANYTHING BELOW THIS
####################################




f = open('A2P1_RumbaSim_' + name + '_output.txt', 'w')

f.write(f'{name}\n')
f.write(f'{header1}\n')
f.write(f'{header2}\n\n\n')
   

p = .1
vacP = -1
moveP = -1
oneP = 1
twoP = 2

myAgent = Agent(name, p, vacP, moveP, oneP, twoP)
rumba_simulation(f, myAgent, p, vacP, moveP, oneP, twoP)


p = .2
vacP = -.4
moveP = -.3
oneP = 1
twoP = 3

myAgent = Agent(name, p, vacP, moveP, oneP, twoP)
rumba_simulation(f, myAgent, p, vacP, moveP, oneP, twoP)



p = .4
vacP = -.4
moveP = -.3
oneP = 1
twoP = 3

myAgent = Agent(name, p, vacP, moveP, oneP, twoP)
rumba_simulation(f, myAgent, p, vacP, moveP, oneP, twoP)



p = .05
vacP = -.5
moveP = -.3
oneP = 2
twoP = 5

myAgent = Agent(name, p, vacP, moveP, oneP, twoP)
rumba_simulation(f, myAgent, p, vacP, moveP, oneP, twoP)


f.close()




 




