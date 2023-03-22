from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __str__(self) -> str:
        return f"Ponto ({self.x}, {self.y})"
