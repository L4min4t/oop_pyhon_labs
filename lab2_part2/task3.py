# The class GROUP contains a sequence 
# of instances of the class STUDENT.
# The class STUDENT contains the 
# student's name, surname, record book number
# and grades.
# Determine the required attributes-data 
# and attributes-methods in classes GROUP and STUDENT.
# Find the average score of each student. 
# Output to the standard output stream the five 
# students with the highest average score.
# Assume that there can be no more than 20 students
# in a group, as well as students with 
# the same name and surname.

from Record_book import Record_book
from Student import Student
from Group import Group

def main():
    try:
        record_book1 = Record_book([100, 20, 12, 13])
        record_book2 = Record_book([32, 15, 5])
        record_book3 = Record_book([36, 95, 5])
    
        student1 = Student('Ivan', 'Vlasiuk', record_book1)
        student2 = Student('Igor', 'Feschuk', record_book2)
        student3 = Student('Artem', 'Mekhanikov', record_book3)
        group1 = Group(student1, student2, student3)
        print(group1.best_students(0))
    except (ValueError, TypeError) as exc:
        print(exc)
if __name__ == '__main__':
    main()