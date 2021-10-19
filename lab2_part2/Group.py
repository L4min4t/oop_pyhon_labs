from Student import Student

class Group:
    def __init__(self, *student_list):
        self.students = student_list
        self.__amount_of_students = len(student_list)
        

    @property
    def amount_of_student(self):
        return self.__amount_of_students

    @property
    def students(self):
        return self.__students
    
    @students.setter
    def students(self, student_list):
        if not student_list:
            raise ValueError('group must contains students')
        if len(student_list) > 20:
            raise ValueError('group must contains less than 20 students')
        if isinstance(all(student_list), Student):
            raise TypeError('students must be Student type')
        if self.__is_contains_duplicate_names(student_list):
            raise ValueError('group cann\'t contain students with equals name/surname')
        self.__students = list(student_list)

    def best_students(self, number):
        if not isinstance(number, int):
            raise TypeError('amount of best students must be int')
        if number > len(self.students) or number < 0:
            raise ValueError('amount of best students must be in range 0 to amount of students')

        best_students = {}
        result = ''

        for stud in self.students:
            best_students.update({stud.record_book.average_score : f'{stud.name} {stud.surname}'})
        students_rating_table = dict(sorted(best_students.items(), reverse = True)[0:number])

        for key in students_rating_table:
            result += str(key) + '\t' + students_rating_table[key] + '\n'

        return result[0:-1]


    def add_students(self, student):
        if self.__is_contains_duplicate_names(self.students + [student]):
            raise ValueError('group cann\'t contain students with equals name/surname')
        if not isinstance(student, Student):
            raise TypeError('u can add only students')
        self.students.append(student)
        self.__amount_of_students += 1

    def del_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('u can delete only student')
        self.__students.remove(student)
        self.__amount_of_students -= 1

    def __is_contains_duplicate_names(self, student_list):
        names = []
        for stud in student_list:
            names.append(stud.name)
            names.append(stud.surname)
        return len(names) != len(set(names))

    def __str__(self) -> str:
        group = f'amount of students = {self.amount_of_student}\n\nstudents:\n'
        for stud in self.students:
            group += str(stud) + '\n\n'
        return group[0:-2]
