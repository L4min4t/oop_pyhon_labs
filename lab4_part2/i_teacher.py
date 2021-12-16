from abc import abstractmethod


class ITeacher:
    """"
    interface for teacher
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
    def courses(self):
        """
        propery courses
        """
        pass

    @courses.setter
    @abstractmethod
    def courses(self, value):
        """
        setter propery courses
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        class transformation in string
        """
        pass
