import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(1, 2)
point2 = Point(4, 6)

print("Координаты точки 1: ", point1.get_coordinates())
print("Координаты точки 2: ", point2.get_coordinates())

distance = point1.distance_to(point2)
print("Расстояние между точками: ", distance)

point1.set_coordinates(3, 4)
print("Новые координаты точки 1: ", point1.get_coordinates())
