from subject import Subject

while(True):
    chooseEvent = raw_input('''
To add assignment: Type a
To Mark as done: Type m
To Delete Assignment: Type d
To list all assignments: Type l:
To exit: Type x
''')

    if(chooseEvent == "a"):#add assignments
        f = open("../dataFiles/user.txt", "a+")
        event = raw_input("Enter an assignment: ")
        math = Subject()
        math.addAssignment(f, event)
        print("Successfully added assignment")
        f.close()

    elif(chooseEvent == "l"):#list assignments
        f = open("../dataFiles/user.txt", "r")
        print("Here is a list of your assignments")

        readline = f.read()

        print(readline)
        f.close()

    elif(chooseEvent == "m"):#mark assignment as done
        assignmentToMark = raw_input('''Which assignment do you want to change the status of?
''')

        math = Subject()
        math.markAsDone(assignmentToMark)


    elif(chooseEvent == "d"):#delete assignment
        chooseAssignment = raw_input('''Which assignment do you want to delete?
''')

        math = Subject()
        math.deleteAssignment(chooseAssignment)


    elif(chooseEvent == "x"):#exit
        exit()

    else:
        print(chooseEvent + " is not valid")