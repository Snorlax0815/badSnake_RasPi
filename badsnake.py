from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import signal
import sys
import os

from random import randint
from sense_hat import SenseHat


class Array:
    MIN = 0
    MAX = 63

    @staticmethod
    def get_random_snake():
        p1 = Array.get_random()
        p2 = [p1[0]]
        if p1[1] < 7:
            p2.append(p1[1] + 1)
        else:
            p2.append(p1[1] - 1)
        return [p1, p2]

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
        return [row, col]

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


SOUTH = 1
EAST = 2
NORTH = 3
WEST = 4


class Snake:
    def __init__(self):
        self.points = Array.get_random_snake()

    def set_point(self, p):
        """
        set new head point

        :param p:
        :return:
        """
        self.points.insert(0, p)

    def move(self, direction, apple=None):
        """
        move in the given direction

        :param apple:
        :param direction:
        :return:
        """
        point = self.points[0]
        h = point
        #h = Array.convert_to_array(point)
        if direction == SOUTH:
            h_neu = [h[0] + 1, h[1]]
        elif direction == EAST:
            h_neu = [h[0], h[1] + 1]
        elif direction == NORTH:
            h_neu = [h[0] - 1, h[1]]
        else:
            h_neu = [h[0], h[1] - 1]

        if h_neu in self.points:
            # bite the body
            return -1

        if Array.is_correct_value(h_neu) is False:
            # point is outside
            return -2

        self.set_point(h_neu)
        # move forward
        if apple is not None:
            if apple != h_neu:
                # didn't eat the apple
                self.points.pop()
                # remove last element
                return 1
            else:
                # ate the apple
                return 0

    def get_snake(self):
        return self.array


H = [0, 0, 255]  # Head: blue
A = [255, 0, 0]  # Apple: red
B = [0, 255, 0]  # Body: green
F = [0, 0, 0]  # Free: white


class LED_Matrix:
    def __init__(self):
        self.array = [
            F, F, F, F, F, F, F, F,
            F, F, F, F, F, F, F, F,
            F, B, B, H, F, A, F, F,
            F, B, F, F, F, F, F, F,
            F, F, F, F, F, F, F, F,
            F, F, F, F, F, F, F, F,
            F, F, F, F, F, F, F, F,
            F, F, F, F, F, F, F, F
        ]
        self.clear()

    def clear(self):
        for i in range(len(self.array)):
            self.array[i] = F

    def paint_snake(self, snake):
        for i in range(len(snake)):
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

    def get_display(self):
        return self.array


class Game:
    CTRT = "You lost!"
    CTRC = [255, 128, 0]

    def __init__(self):
        self.s = Snake()  # snake
        self.d = LED_Matrix()
        self.a = None  # apple
        self.create_apple()
        self.sense = SenseHat()
        # callback methods for joystick signals
        self.sense.stick.direction_up = self.up
        self.sense.stick.direction_down = self.down
        self.sense.stick.direction_left = self.left
        self.sense.stick.direction_right = self.right
        self.sense.stick.direction_any = self.refresh
        self.sense.stick.direction_middle = self.enter

    def up(self, event):
        if event.action != ACTION_RELEASED:
            eat = self.s.move(NORTH, self.a)
            self.moved(eat)

    def right(self, event):
        if event.action != ACTION_RELEASED:
            eat = self.s.move(EAST, self.a)
            self.moved(eat)

    def down(self, event):
        if event.action != ACTION_RELEASED:
            eat = self.s.move(SOUTH, self.a)
            self.moved(eat)

    def left(self, event):
        if event.action != ACTION_RELEASED:
            eat = self.s.move(WEST, self.a)
            self.moved(eat)

    def moved(self, eaten):
        if eaten == -2 | eaten == -1:
            self.enter() # lost
        elif eaten == 0:
            self.create_apple()
        self.refresh()

    def refresh(self):
        self.d.paint_snake(self.s.points)
        self.d.paint_apple(self.a)
        self.sense.set_pixels(self.d.get_display())

    def create_apple(self):
        while self.a is None:
            self.a = Array.get_random()
            if self.a in self.s.points:
                self.a = None

    def enter(self, event):
        """
        the joystick event, if direction middle was used
        :param event: signal from joystick (action: ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED)
        """
        if event.action != ACTION_RELEASED:
            # send keyboard interrupt to active process
            os.kill(os.getpid(), signal.SIGINT)

    def msg(self, text, color):
        """
        shows the message in given color
        :param text: text to print
        :param color: color for the text
        """
        self.sense.clear()
        self.sense.show_message(text, text_colour=color)
        self.sense.clear()

    def run(self):
        while True:
            self.refresh()
            try:
                # wait, until an event occurs
                signal.pause()
            except KeyboardInterrupt:
                # if CRTL_C event was fired or direction middle was used.
                # send a "goodbye" message and exit script
                self.msg(Game.CTRT, Game.CTRC)
                break;


if __name__ == '__main__':
    g = Game()
    g.run()
