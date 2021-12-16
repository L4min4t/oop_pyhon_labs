from i_course import ICourse
from teacher import Teacher


class Course(ICourse):
    """
    class implemets ICourse
    """
    def __init__(self, name, teacher, program):
        """
        class constructor
        """
        self.name = name
        self.teacher = teacher
        self.program = program

    @property
    def name(self):
        """
        propery name
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        setter propery name
        """
        if not isinstance(value, str):
            raise TypeError('name must be str')
        if not value.strip():
            raise ValueError('name can\'t be empty')
        self.__name = value

    @property
    def teacher(self):
        """
        propery teacher
        """
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        """
        setter propery teacher
        """
        if not isinstance(value, Teacher):
            raise TypeError('teacher must be Teacher type')
        self.__teacher = value

    @property
    def program(self):
        """
        propery program
        """
        return self.__program

    @program.setter
    def program(self, value):
        """
        setter propery program
        """
        if not isinstance(value, str):
            raise TypeError('program must be str type')
        self.__program = value

    def __str__(self) -> str:
        """
        class transformation in string
        """
        return f'Local course: {self.name}, Teacher: {self.teacher.name}, Program: {self.program}'
