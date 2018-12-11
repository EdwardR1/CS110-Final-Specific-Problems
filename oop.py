# Create a class called “Subject”
    # Constructor asking for a name and grade (Both should be private variables)
    # String method printing out the name of the class and the grade
    # Method / Function to get and set both variables
# Create a class called “Student”
    # Constructor asking for a name and a list of “Subjects”
    # String method printing out the name of the student and the classes student is taking, along with grades associated with it
    # Method / Function to get and set List of Subjects , and specific classes in the list
    # Method / Function to calculate GPA for the student


class Subject:
    pass



class Student:
    pass


def test():
    John = Student("John", [Subject("Introduction to Computer Science 1", "A"), Subject("Calculus 1", "A-")])
    print(John.getName()) # Should print out "John"
    CS1 = John.getSubjectByName("Introduction to Computer Science 1")
    print(CS1.getName()) # Should print out "Introduction to Computer Science 1"
    print(CS1.getGrade()) # Should print out "A"

test()
