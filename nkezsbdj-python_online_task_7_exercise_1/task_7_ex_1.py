"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Code like ArrayRectangles(Rectangle(),[Rectangle(),Rectangle()]) should be valid;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, a: float = 4.0, b: float = 3.0):
        self.__side_a = a
        self.__side_b = b
        if a < 0 or b < 0:
            raise ValueError

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return self.__side_a * 2 + self.__side_b * 2

    def is_square(self):
        a_sides = self.__side_a * 2
        b_sides = self.__side_b * 2
        if a_sides == b_sides:
            return True
        else:
            return False

    def replace_sides(self):
        self.__side_a, self.__side_b = self.__side_b, self.__side_a


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = []
        if not type(n) is int:
            raise TypeError
        if n < 0:
            raise ValueError
        for rectangles in args:
            if isinstance(rectangles, list):
                self.__rectangle_array.extend(rectangles)
            else:
                if not isinstance(rectangles, Rectangle):
                    raise TypeError
                else:
                    self.__rectangle_array.append(rectangles)
        while n - len(self.__rectangle_array) > 0:
            self.__rectangle_array.append(None)

    def add_rectangle(self, rectangle):
        if None in self.__rectangle_array:
            self.__rectangle_array[self.__rectangle_array.index(None)] = rectangle
            return True
        else:
            return False

    def number_max_area(self):
        all_area = []
        for rectangle in self.__rectangle_array:
            all_area.append(rectangle.area())
        return all_area.index(max(all_area))

    def number_min_perimeter(self):
        all_perimeters = []
        for rectangle in self.__rectangle_array:
            all_perimeters.append(rectangle.perimeter())
        return all_perimeters.index(min(all_perimeters))

    def number_square(self):
        squares = []
        for rectangle in self.__rectangle_array:
            if rectangle.is_square() is True:
                squares.append(rectangle)
        return len(squares)
