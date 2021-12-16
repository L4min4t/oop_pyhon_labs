from abc import ABCMeta, abstractmethod


class ICourse(metaclass=ABCMeta):
    """
    intarface for courses
    """
    @property
    @abstractmethod
    def name(self):
        """
        propery name
        """
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        """
        setter propery name
        """
        pass

    @property
    @abstractmethod
    def teacher(self):
        """
        propery teacher
        """
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        """
        setter propery teacher
        """
        pass

    @property
    @abstractmethod
    def program(self):
        """
        propery program
        """
        pass

    @program.setter
    @abstractmethod
    def program(self, value):
        """
        setter propery program
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        class transformation in string
        """
        pass
