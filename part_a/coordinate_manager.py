from typing import List, Dict

from part_a.coordinate import Coordinate
from part_a.point import Point
from utils import format_number


class CoordinateManager:
    __coordinates: List[Coordinate] = []

    def __init__(self, origin: Point):
        self.__origin = origin

    def add(self, point: Point) -> None:
        self.__coordinates.append(Coordinate(
            self.__origin,
            point
        ))

    def quadrant_count(self) -> Dict[int, int]:
        count: Dict[int, int] = {
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }

        for coordinate in self.__coordinates:
            quadrant = coordinate.quadrant

            if quadrant == 0:
                continue

            count[quadrant] += 1

        return count

    def get_nearest_and_farthest(self) -> List[Coordinate]:
        self.__coordinates = sorted(
            self.__coordinates,
            key=lambda attribute: attribute.euclidean_distance
        )

        return [self.__coordinates[0], self.__coordinates[-1]]

    def print_coordinates_quadrant(self) -> None:
        for coordinate in self.__coordinates:
            print(coordinate)

    def print_nearest_and_farthest(self) -> None:
        nearest, farthest = self.get_nearest_and_farthest()

        print(f"{nearest.point} é o mais próximo, distância={format_number(nearest.euclidean_distance)}")
        print(f"{farthest.point} é o mais distante, distância={format_number(farthest.euclidean_distance)}")

    def print_quadrant_count(self) -> None:
        count = self.quadrant_count()
        print(
            f"Existe(m) {count[1]} ponto(s) no 1º quadrante; {count[2]} no 2º quadrante; {count[3]} no 3º quadrante e {count[4]} no 4º quadrante.")
