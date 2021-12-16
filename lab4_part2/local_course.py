from i_local_course import ILocalCourse
from course import Course


class LocalCourse(Course, ILocalCourse):
    """
    class extends Course and implemets ILocalCourse
    """
    def __init__(self, name, teacher, room, program):
        """
        class constructor
        """
        self.room = room
        super().__init__(name, teacher, program)

    @property
    def room(self):
        """
        propery room
        """
        return self.__room

    @room.setter
    def room(self, value):
        """
        setter propery room
        """
        if not isinstance(value, str):
            raise TypeError('room must be str type')
        self.__room = value

    def __str__(self) -> str:
        """
        class transformation in string
        """
        return f'Local course: {self.name}, Room: {self.room}, Teacher: {self.teacher.name}, Program: {self.program}'
