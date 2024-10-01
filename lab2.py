import math
import numpy as np  # Внешний пакет
from abc import ABC, abstractmethod


# Абстрактный класс "Геометрическая фигура"
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


# Класс "Цвет фигуры"
class Color:
    def __init__(self):
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


# Класс "Прямоугольник"
class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color()
        self.color.color = color

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Площадь: {:.2f}".format(
            self.FIGURE_TYPE, self.color.color, self.area()
        )


# Класс "Круг"
class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color()
        self.color.color = color

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Площадь: {:.2f}".format(
            self.FIGURE_TYPE, self.color.color, self.area()
        )


# Класс "Квадрат"
class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side_length, color):
        super().__init__(side_length, side_length, color)

    def __repr__(self):
        return "Фигура: {}, Цвет: {}, Площадь: {:.2f}".format(
            self.FIGURE_TYPE, self.color.color, self.area()
        )


# Функция main для тестирования классов
def main():
    N = 5
    M = 7# Пример значения N

    rect = Rectangle(N, M, "синий")
    circ = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(rect)
    print(circ)
    print(square)

    # Используем внешний пакет numpy
    arr = np.array([1, 2, 3, 4, 5])
    print("Массив из numpy:", arr)


if __name__ == "__main__":
    main()
