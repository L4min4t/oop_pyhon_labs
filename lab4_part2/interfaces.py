from abc import ABCMeta, abstractmethod

class ICourse(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @program.setter
    @abstractmethod
    def program(self, value):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class ITeacher:
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass

    @courses.setter
    @abstractmethod
    def courses(self, value):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class ILocalCourse(ICourse):
    @property
    @abstractmethod
    def room(self):
        pass

    @room.setter
    @abstractmethod
    def room(self, value):
        pass


class IOffsiteCourse(ICourse):
    @property
    @abstractmethod
    def town(self):
        pass

    @town.setter
    @abstractmethod
    def town(self, value):
        pass


class ICourseFactory:
    @abstractmethod
    def pack(self, *args):
        pass

    @abstractmethod
    def unpack(self):
        pass
