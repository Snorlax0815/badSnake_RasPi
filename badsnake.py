from random import randint


class Array:
    def __init__(self):
        self.min = 0
        self.max = 63

    def get_random(self):
        v = randint(self.min, self.max)
        return Array.convert_to_array(v)

    @staticmethod
    def convert_to_list(r, c):
        """
        convert array element to list

        :param r: row
        :param c: colum
        :return: index in list
        """
        return r*8+c

    @staticmethod
    def convert_to_array(v):
        """
        connvert list to array element

        :param v: value in list
        :return:
        """
        row = v/8
        col = v - row * 8
        return row, col


if __name__ == '__main__':
    a = Array()
    print(a.get_random())
    print(Array.convert_to_array(62))
    print(Array.convert_to_list(0, 7))