from abc import abstractmethod
from i_course import ICourse


class ILocalCourse(ICourse):
    """
    interface that implemets ICourse
    """
    @property
    @abstractmethod
    def room(self):
        """
        propery room
        """
        pass

    @room.setter
    @abstractmethod
    def room(self, value):
        """
        setter propery room
        """
        pass
