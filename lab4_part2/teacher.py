from i_teacher import ITeacher


class Teacher(ITeacher):
    """
    class implements ITeacher
    """
    def __init__(self, name, courses):
        """
        class constructor
        """
        self.name = name
        self.courses = courses

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
    def courses(self):
        """
        propery courses
        """
        return self.__courses

    @courses.setter
    def courses(self, value):
        """
        setter propery courses
        """
        if not isinstance(value, str):
            raise TypeError('courses must be str')
        self.__courses = value

    def __str__(self) -> str:
        """
        class transformation in string
        """
        return f'Teacher: {self.name}  Courses: {self.courses}'
