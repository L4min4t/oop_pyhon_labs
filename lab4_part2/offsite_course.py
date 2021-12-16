from i_offsite_course import IOffsiteCourse
from course import Course


class OffsiteCourse(Course, IOffsiteCourse):
    """
    class extends Course and implemets IOffsiteCourse
    """
    def __init__(self, name, teacher, town, program):
        """
        class constructor
        """
        self.town = town
        super().__init__(name, teacher, program)

    @property
    def town(self):
        """
        propery town
        """
        return self.__town

    @town.setter
    def town(self, value):
        """
        setter propery town
        """
        if not isinstance(value, str):
            raise TypeError('town must be str type')
        self.__town = value

    def __str__(self) -> str:
        """
        class transformation in string
        """
        return f'Offsite course: {self.name}, Town: {self.town}, Teacher: {self.teacher.name}, Program: {self.program}'
