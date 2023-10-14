class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width
        self.side = width

    def set_height(self, height):
        self.height = height
        self.side = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal
    
    def get_picture(self):
        line = ''
        if self.height and self.width > 50:
            return f"Too big for picture."
        for i in range(self.height):
            line += ('*' * self.width)+'\n'
        return line
    
    def get_amount_inside(self, shape):
        area_self = self.get_area()
        area_shape = shape.get_area()
        amt = int(area_self / area_shape)
        return amt
       
class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.side})"
    
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
sq.set_width(4)
print(str(sq))

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))