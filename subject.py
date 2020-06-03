class Subject:

    def __init__(self):
        pass

    def deleteAssignment(self, assignmentToDelete):
        flag = False
        with open("../dataFiles/user.txt", "r+") as f:
            allLines = f.readlines()
            f.seek(0)
            for line in allLines:
                partitionPoint = line.partition(":")
                assignment = partitionPoint[0]
                if assignment != assignmentToDelete:
                    f.write(line)
                else:
                    flag = True
            f.truncate()
            f.close()

            if flag == False:
                print("Assignment " + assignmentToDelete + " not found")
            else:
                print("Assignment " + assignmentToDelete + " deleted.")


    def markAsDone(self, changeStatus):
        flag = False

        with open("../dataFiles/user.txt", "r+") as f:
            allLines = f.readlines()
            f.seek(0)
            for line in allLines:
                partitionPoint = line.partition(":")
                status = partitionPoint[2]
                assignment = partitionPoint[0]
                if assignment == changeStatus:
                    if status == 'f\n':
                        f.write('t\n')
                    if status == 't\n':
                        f.write('f\n')

                    print("Status changed")
                    flag = True

            if flag == False:
                print("assignment does not exist")


            f.close()

    def listAssignments(self):
        print("Inside List Assignments")

    def addAssignment(self, file, event):
        file.write(event + ":" + "f" + "\n")