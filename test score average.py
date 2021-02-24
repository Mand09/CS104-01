howManyEntered = 0
total = 0
average = 0
#this line inputs how many test scores user wants average
howMany = input ("How many test scores would you like to average?")
print(howMany)
while howManyEntered < howMany:
    testScore=input("Enter test score")
    total=testScore + total
    howManyEntered=+1
    average=total/howMany
print(average)
