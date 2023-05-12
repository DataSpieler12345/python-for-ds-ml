# A base exception class for our code:
class StudentsDataException(Exception):
    pass


# An exception for erroneous lines:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# An exception for an empty file.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# A dictionary for student data:
data = { }

file_name = input("Enter the student's data file name: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Read the complete file in the list.
    lines = f.readlines()
    f.close()
    # Is the file empty?
    if len(lines) == 0:
        raise FileEmpty()
    # Scan the file line by line.
    for i in range(len(lines)):
        # Obtain line n.
        line = lines[i]
        # Divide it into columns.
        columns = line.split()
        # There must be 3 columns, are they there?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Builds a key from the student's first and last name.
        student = columns[0] + ' ' + columns[1]
        # Obtaining points.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Update the dictionary.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Print results.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("An I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Incorrect line #" + str(e.line_number) + " in the source file:" + e.line_string)
except FileEmpty:
    print("Empty source file")
    