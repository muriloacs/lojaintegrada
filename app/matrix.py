# -*- coding: utf8 -*-

from prettytable import PrettyTable


class Matrix(object):

    # The representation of the matrix itself.
    elements = []

    # A tuple (immutable list) representing all the available parameters.
    available_commands = ('I', 'C', 'L', 'V', 'H', 'K', 'F', 'S', 'X')

    # Matrix saved outputs.
    outputs = []

    # Representation of a white pixel.
    WHITE_PIXEL = [0]

    def create(self, m, n):
        """
        Creates a new matrix containing only white pixels.
        :param m: number of columns
        :param n: number of rows
        """
        self.elements = [self.WHITE_PIXEL * int(m) for row in range(int(n))]

    def clean(self):
        """
        Cleans matrix by switching all elements to white pixels.
        """
        m, n = self.length()
        self.create(m, n)

    def draw_element(self, x, y, color):
        """
        Colors element at position x, y.
        :param x: column
        :param y: row
        :param color: character
        """
        x = abs(int(x))
        y = abs(int(y))
        color = str(color).upper()

        if 0 in (x, y):
            raise ValueError

        self.elements[y-1][x-1] = color

    def draw_column(self, x, y1, y2, color):
        """
        Colors column x from rows y1 to y2.
        :param x: column
        :param y1: starting row
        :param y2: finishing row
        :param color: character
        """
        for y in range(int(y1), int(y2)+1):
            self.draw_element(int(x), y, color)

    def draw_row(self, x1, x2, y, color):
        """
        Colors row y from columns x1 to x2.
        :param x1: starting column
        :param x2: finishing column
        :param y: row
        :param color: character
        """
        for x in range(int(x1), int(x2)+1):
            self.draw_element(x, int(y), color)

    def draw_rectangle(self, x1, y1, x2, y2, color):
        """
        Colors a rectangle.
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param color: character
        """
        for y in range(int(y1), int(y2)+1):
            self.draw_row(int(x1), int(x2), y, color)

    def draw_area(self, x, y, color):
        """
        Colors an area.
        :param x:
        :param y:
        :param color:
        """
        self.fill(int(x) - 1, int(y) - 1, color.upper())

    def fill(self, x, y, color, color_at_position=None):
        """
        Fills area that must be coloured.
        :param x:
        :param y:
        :param color:
        :param color_at_position:
        """
        rows = len(self.elements) - 1
        columns = len(self.elements[0]) - 1

        if color_at_position == None:
            # Gets color at position x, y.
            color_at_position = self.elements[x][y]

        if self.elements[x][y] != color_at_position:
            # Do nothing.
            return

        # Colors element x, y.
        self.elements[x][y] = color

        # Calling recursively.
        if x < rows:
            self.fill(x + 1, y, color, color_at_position)

        if y < columns:
            self.fill(x, y + 1, color, color_at_position)

        if x > 0:
            self.fill(x - 1, y, color, color_at_position)

        if y > 0:
            self.fill(x, y - 1, color, color_at_position)

        return

    def save_image(self, name):
        """
        Saves an image into a file.
        :param name: name of the file
        :return:
        """
        # Save to a file
        with open("images/{0}".format(name), "w") as image_file:
            image_file.write(str(self.to_table(self.elements)))

        # Save to outputs
        self.outputs.append({"name": name, "matrix": self.elements})
        self.clean()

    def show(self):
        """
        Shows created matresses.
        :return:
        """
        for output in self.outputs:
            print("\n", output['name'], self.to_table(output['matrix']))

    @staticmethod
    def to_table(matrix):
        """
        Turns matrix into a table.
        :return: table
        """
        table = PrettyTable()

        for row in matrix:
            table.add_row(row)

        return table

    def length(self):
        """
        Returns the size of the matrix as a tuple.
        :return:
        """
        m = len(self.elements[0])
        n = len(self.elements)

        return m, n


def main():
    """
    Everything starts here.
    """
    matrix = Matrix()

    while True:
        program_input = input("Input: ")
        parameters = program_input.split(' ')
        command = parameters[0].upper()

        if command not in matrix.available_commands:
            continue

        elif command == 'I':
            matrix.create(parameters[1], parameters[2])

        elif command == 'C':
            matrix.clean()

        elif command == 'L':
            matrix.draw_element(parameters[1], parameters[2], parameters[3])

        elif command == 'V':
            matrix.draw_column(parameters[1], parameters[2], parameters[3], parameters[4])

        elif command == 'H':
            matrix.draw_row(parameters[1], parameters[2], parameters[3], parameters[4])

        elif command == 'K':
            matrix.draw_rectangle(parameters[1], parameters[2], parameters[3], parameters[4], parameters[5])

        elif command == 'F':
            matrix.draw_area(parameters[1], parameters[2], parameters[3])

        elif command == 'S':
            matrix.save_image(parameters[1])

        elif command == 'X':
            matrix.show()
            print("Program exited.")
            break

if __name__ == '__main__':
    main()
