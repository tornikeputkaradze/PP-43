class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f"{self.name}: ფართობი = {self.area()}")


class Rectangle(Shape):
    def __init__(self, width, height, name="მართკუთხედი"):
        super().__init__(name)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("სიგანე უნდა იყოს დადებითი")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("სიმაღლე უნდა იყოს დადებითი")
        self.__height = value

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side, "კვადრატი")


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("რადიუსი უნდა იყოს დადებითი")
        super().__init__("წრე")
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius ** 2, 2)


def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return round(total, 2)


def largest(shapes):
    return max(shapes, key=lambda shape: shape.area())


shapes = [Rectangle(4, 5), Square(3), Circle(2), Shape("უცნობი ფიგურა")]

for shape in shapes:
    shape.info()

print("ჯამური ფართობი:", total_area(shapes))
print("უდიდესი:", largest(shapes).name)

rectangles = [shape for shape in shapes if isinstance(shape, Rectangle)]
print("მართკუთხედების რაოდენობა (კვადრატის ჩათვლით):", len(rectangles))

try:
    Circle(-3)
except ValueError as error:
    print("შეცდომა:", error)

try:
    Square(0)
except ValueError as error:
    print("შეცდომა:", error)