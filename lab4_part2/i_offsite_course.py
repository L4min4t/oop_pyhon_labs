from abc import abstractmethod
from i_course import ICourse


class IOffsiteCourse(ICourse):
    """
    interface that implemets ICourse
    """
    @property
    @abstractmethod
    def town(self):
        """
        propery town
        """
        pass

    @town.setter
    @abstractmethod
    def town(self, value):
        """
        setter propery town
        """
        pass
