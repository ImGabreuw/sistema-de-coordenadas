from part_a.coordinate_manager import CoordinateManager
from part_a.point import Point
from utils import int_list_input, int_input


def entry():
    x, y = int_list_input("Digite as coordenadas da origem translada no seguinte formato 'x y': ")
    n = int_input("Digite o número de pontos a serem lidas: ")

    manager = CoordinateManager(Point(x, y))

    for i in range(1, n + 1):
        a, b = int_list_input(f"Digite as coordenadas do {i}o ponto: ")
        manager.add(Point(a, b))

    manager.print_coordinates_quadrant()
    manager.print_nearest_and_farthest()
    manager.print_quadrant_count()
