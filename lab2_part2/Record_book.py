class Record_book:
    id_generator = 0
    def __init__(self, grades):
        self.grades = grades
        self.id = Record_book.id_generator
        Record_book.id_generator += 1

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("ID must be int")
        if value < Record_book.id_generator:
            raise ValueError("ID generation failure")
        self.__id = value
        
    @property   
    def average_score(self):
        return self.__average_score

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, list):
            raise TypeError('grades must be list')
        if not isinstance(all(grades), int):
            raise TypeError('grades must be int')
        if not all(ele >= 0 and ele <= 100 for ele in grades):
            raise ValueError('grades must be in 0 to 100 range')
        self.__grades = grades
        self.__average_score = round(sum(self.grades) / len(self.grades), 2)

            

    def add_grades(self, *grades):
        if not isinstance(grades, tuple):
            raise TypeError('grades must be tuple')
        if not isinstance(all(grades), int):
            raise TypeError('grades must be int')
        for i in grades:
            self.grades += i
        self.__average_score = round(sum(self.grades) / len(self.grades), 2)

    def del_grades(self, grade):
        if not isinstance(grade, int):
            raise TypeError('grade must be int')
        self.__grades.remove(grade)
        self.__average_score = round(sum(self.grades) / len(self.grades), 2)

    def __str__(self) -> str:
        return f'grades: {self.grades}\naverage score: {self.average_score}'
