#Create a class Rectangle with attributes length and width, each of which defaults to 1.\
#Provide methods that calculate the perimeter and the area of the rectangle.
#Also, provide setter and getter for the length and width attributes.
#The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.

class Rectangle:
    """
    class that containt rectangle with sides less than 20.0
    sides must be initialized by floating-point numbers
    also class can calculate area and perimetr
    """
    def __init__(self, length = 1., width = 1.):
        if not(isinstance(width, float)) or not(isinstance(length, float)):
            raise TypeError ('type must by float')
        elif length <= 0 or length > 20 or width < 0 or width > 20:
            raise ValueError('0 <= side <= 20')
        self.__length = length
        self.__width = width
    
    def calculate_perimetr(self):
        return 2*(self.__width + self.__length)

    def calculate_area(self):
        return self.__width * self.__length

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if not(isinstance(length, float)): 
            raise TypeError ('type must by float')
        elif length <= 0 or length > 20:
            raise ValueError('0 <= side <= 20')
        self.__length = length

    @width.setter
    def width(self, width):
        if not(isinstance(width, float)):
            raise TypeError ('type must by float')
        elif width < 0 or width > 20:
            raise ValueError('0 <= side <= 20')
        self.__width = width

    @length.getter
    def get_length(self):
        return self.__length

    @width.getter
    def get_width(self):
        return self.__width

def main():
    try:
        rec = Rectangle(2.3, 2.2)
        rec.width = 2.5
        rec.length = 2.5
        print(rec.calculate_area())
        print(rec.get_width)
    except Exception as exc:
        print(exc)

main()