#Tuples and dictionaries can work together

#Let's imagine the following problem:

#you need a program to calculate the averages of your students;

#the program asks for the student's name followed by his or her grade;

#the names are entered in any order;

#entering an empty name terminates the data entry (Note 1: entering an empty score will generate the ValueError exception, but don't worry about that now, you will see how to handle such cases when we talk about exceptions in the second part of the course series) a list with all the names and the average of each student should be displayed at the end.


school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's grade (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)