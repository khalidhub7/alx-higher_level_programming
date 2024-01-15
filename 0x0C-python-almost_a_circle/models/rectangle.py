class Rectangle(Base):
    '''rectangle class'''


    def __init__(self, width, height, x=0, y=0, id=None):
        '''class'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''get / set'''
        return self.__width

    @width.setter
    def width(self):
        self.__width = self.__width

    @property
    def height(self):
        '''get / set'''
        return self.__height

    @height.setter
    def height(self):
        self.__height = self.__height

    @property
    def x(self):
        '''get / set'''
        return self.__x

    @height.setter
    def x(self):
        self.__x = self.__x

    @property
    def y(self):
        '''get / set'''
        return self.__y

    @height.setter
    def y(self):
        self.__y = self.__y
