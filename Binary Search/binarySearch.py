import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
print(elementsList[0])

# print the last element
print(elementsList[len(elementsList)-1])
# print all the elements
print(elementsList)

# Start your search algorithm here.
start = 0
end = len(elementsList)-1

index = int((end - start)/2)

print(" ")
print("type a country or n for a number")
Find = (input("What Country?: "))


loop = 0
notFound = True
while notFound == True:
    if loop == 10:
        print ("I'm stuck")
        print (":(")
        print ("did you forget to type n?")
        notFound = False
    elif Find == ("n"):
        number = int(input("put a number: "))
        index = number-1
        print(" ")
        print(elementsList[index])
        print("is the")
        if number == 1:
            print(str(number)+"st")
        elif number == 2:
            print(str(number)+"nd")
        elif number == 3:
            print(str(number)+"rd")
        elif number > 3:
            print(str(number)+"th")
        print("country in this list")
        notFound = False
    else:
        if Find == elementsList[index]:
            print(" ")
            print(Find)
            print("is the")
            if index == 0:
                print(str(index+1)+"st")
            elif index == 1:
                print(str(index+1)+"nd")
            elif index == 2:
                print(str(index+1)+"rd")
            elif index > 2:
                print(str(index+1)+"th")
            print("country in this list")
            notFound = False
        elif Find < elementsList[index]:
            end = index
            index = int((end - start)/2) + start
            loop += 1
            print ("looped")
            notFound = True
        elif Find > elementsList[index]:
            start = index
            index = int((end - start)/2) + start
            loop += 1
            print ("looped")
            notFound = True
