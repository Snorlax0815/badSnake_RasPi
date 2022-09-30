from random import randint


class Array:
    MIN = 0
    MAX = 63

    @staticmethod
    def get_random():
        v = randint(Array.MIN, Array.MAX)
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
    print(Array.get_random())
    print(Array.convert_to_array(62))
    print(Array.convert_to_list(0, 7))