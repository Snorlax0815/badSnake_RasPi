from random import randint
from sense_hat import SenseHat


class Array:
    MIN = 0
    MAX = 63

    @staticmethod
    def get_random():
        v = randint(Array.MIN, Array.MAX)
        return Array.convert_to_array(v)

    @staticmethod
    def convert_to_list(r, c=None):
        """
        convert array element to list

        :param r: row
        :param c: colum
        :return: index in list
        """
        if type(r) == list and c is None:
            r, c = r
        return r * 8 + c

    @staticmethod
    def convert_to_array(v):
        """
        connvert list to array element

        :param v: value in list
        :return: array element (r,c)
        """
        row = v / 8
        col = v - row * 8
        return row, col

    @staticmethod
    def is_correct_value_a(r, c):
        """
        Is this point within the array
        :param r: row
        :param c: colum
        :return: True /False
        """
        v = Array.convert_to_list(r, c)
        return Array.correct_value(v)

    @staticmethod
    def is_correct_value(v):
        """
        Is this point within the array
        :param v: index of the list or array element
        :return: True /False
        """
        if type(v) == list:
            r, c = v
            v = Array.convert_to_list(r, c)

        return v >= Array.MIN & v <= Array.MAX


class Snake:
    S = 1  # south
    E = 2  # east
    N = 3  # north
    W = 4  # west

    def __init__(self):
        self.points = []

    def set_point(self, p):
        """
        set new head point

        :param p:
        :return:
        """
        self.points.insert(0, p)


class LED_Matrix:
    H = [0, 0, 255]  # Head: blue
    A = [255, 0, 0]  # Apple: red
    B = [0, 255, 0]  # Body: green
    F = [0, 0, 0]  # Free: white

    def __init__(self):
        self.array = list
        self.clear()

    def clear(self):
        for i in range(self.array.len()):
            self.array[i] = LED_Matrix.F

    def paint_snake(self, snake):
        for i in range(snake.len()):
            v = Array.convert_to_list(snake[i])
            if i == 0:
                # paint head
                self.array[v] = H
            else:
                # paint body
                self.array[v] = B

    def paint_apple(self, apple):
        v = Array.convert_to_list(apple)
        self.array[v] = A

    def refresh(self, s):
        s.set_pixels(self.array)


if __name__ == '__main__':
    H = [0, 0, 255]  # Head: blue
    A = [255, 0, 0]  # Apple: red
    B = [0, 255, 0]  # Body: green
    F = [0, 0, 0]  # Free: white
    s = SenseHat()
    array = [
        F, F, F, F, F, F, F, F,
        F, F, F, F, F, F, F, F,
        F, B, B, H, F, A, F, F,
        F, B, F, F, F, F, F, F,
        F, F, F, F, F, F, F, F,
        F, F, F, F, F, F, F, F,
        F, F, F, F, F, F, F, F,
        F, F, F, F, F, F, F, F
    ]
    s.set_pixels(array)
"""
if __name__ == '__main__':
    print(Array.get_random())
    print(Array.convert_to_array(62))
    print(Array.convert_to_list(0, 7))
"""
