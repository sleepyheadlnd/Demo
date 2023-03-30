import random

originL = ['Abbaad', 'Carlos', 'Daniel', 'Dario', 'Fabian', 'Ghazwan', 'Hanif', 'Ianko', 'Isaac',
           'Jacob', 'Jj', 'John Michael', 'Jonathan', 'Jordi', 'Jose', 'Khaled', 'Khanh', 'Kusoe',
           'Maicky', 'Mit', 'Muawiyah', 'Nicole', 'Nomin', 'Olvin', 'Vraj', 'Vratik']

#classList=["Isaac", "Jordi","Nomin","Abbaad","Khanh", "John Michael",
#            "Jonathan", "Jose", "Ghazwan","Nicole","Hanif","Olvin","Fabian","Mit","Maicky",
#            "Carlos","Dario","Jj","Jacob","Vraj","Vratik","Daniel","Kusoe","Ianko","Khaled","Muawiyah"]

classList = ['Abbaad','Carlos', 'Daniel', 'John Michael', 'Dario', 'Ghazwan','Isaac',
             'Jacob', 'Jj', 'Jonathan', 'Jordi', 'Jose', 'Khaled', 'Khanh', 'Kusoe',
             'Maicky','Nomin', 'Olvin','Nicole','Vraj', 'Vratik']

print("Class number: ", len(classList))
dupL = classList.copy()

groupNumb = int(input("Enter the number of groups: "))
totalG =[]
x=1
memberNumb = int(len(classList)/groupNumb)
sastified = False

while not sastified:

    for i in range(1,groupNumb+1):

        groupList = []
        while (len(groupList) < memberNumb):
            randNum = random.randint(0, len(classList)-1)
            groupList.append(classList[randNum])
            del classList[randNum]
        groupList.sort()
        totalG.append(groupList)

    for j in range(len(classList)):

        randNum = random.randint(0, len(classList) - 1)
        totalG[j].append(classList[randNum])
        totalG[j].sort()
        del classList[randNum]

    for list in totalG:

        print(f'Group {x}: {list}')
        x += 1

    inp = input('Satisfied with the list?(Y/N) ')
    if inp.lower() == 'y':
        sastified = True
    else:
        classList = dupL.copy()
        print()
        x = 1
        totalG = []
