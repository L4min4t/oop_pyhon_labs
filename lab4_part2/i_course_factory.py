from abc import abstractmethod


class ICourseFactory:
    """
    adstract factory for pack and unpack courses and teachers
    """
    @abstractmethod
    def pack(self, *args):
        """
        method for pack courses and teachers in database
        """
        pass

    @abstractmethod
    def unpack(self):
        """
        method for unpack courses and teachers from database
        """
        pass
