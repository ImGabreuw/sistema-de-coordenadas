import math
from operator import attrgetter

from part_a.point import Point


class Coordinate:
    def __init__(self, origin: Point, point: Point):
        self.origin = origin
        self.point = point
        self.euclidean_distance = self.__get_euclidian_distance()
        self.quadrant = self.__get_quadrant()

    def __str__(self) -> str:
        if self.quadrant == 0:
            return f"{self.point} está sobre o eixo de coordenadas."

        return f"{self.point} está no {self.quadrant}o quadrante."

    def __get_quadrant(self) -> int:
        x, y = attrgetter("x", "y")(self.origin)
        a, b = attrgetter("x", "y")(self.point)

        if a == x or b == y:
            return 0

        if a > x and b > y:
            return 1

        if a < x and b > y:
            return 2

        if a < x and b < y:
            return 3

        if a > x and b < y:
            return 4

    def __get_euclidian_distance(self) -> float:
        x, y = attrgetter("x", "y")(self.origin)
        a, b = attrgetter("x", "y")(self.point)

        return math.sqrt((a - x) ** 2 + (b - y) ** 2)
