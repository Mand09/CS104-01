howManyEntered = 0
total=0
average = 0
howMany = int (input ("How many test scores would you like to average?"))
while (howManyEntered < howMany):
    howManyEntered=howManyEntered + 1
    testScores= input("Enter Test score " + str(howManyEntered)+ ": ")
    testScore=float(testScores)
    total= total+testScore

average= total/howManyEntered    
print("The average of you test scores is: " + str(average) +"%")   

       



