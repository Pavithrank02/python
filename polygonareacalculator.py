class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Setter methods
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # Getter methods
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        # Square is a special case of Rectangle where width == height
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


# Example Usage

# Rectangle Example
rect = Rectangle(5, 10)
print(rect)
print(f"Area: {rect.get_area()}")
print(f"Perimeter: {rect.get_perimeter()}")
print(f"Diagonal: {rect.get_diagonal()}")
print(rect.get_picture())
print(f"Amount of smaller rectangles inside: {rect.get_amount_inside(Rectangle(2, 2))}")

# Square Example
sq = Square(9)
print(sq)
print(f"Area: {sq.get_area()}")
print(f"Perimeter: {sq.get_perimeter()}")
print(f"Diagonal: {sq.get_diagonal()}")
print(sq.get_picture())
