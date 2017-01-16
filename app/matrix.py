# -*- coding: utf8 -*-

from prettytable import PrettyTable


class Matrix(object):

    # The representation of the matrix itself.
    elements = []

    # Matrix saved outputs.
    outputs = []

    # Representation of a white pixel.
    WHITE_PIXEL = [0]

    # All available commands.
    commands = {
        'I': 'create',
        'C': 'clean',
        'L': 'draw_element',
        'V': 'draw_column',
        'H': 'draw_row',
        'K': 'draw_rectangle',
        'F': 'draw_area',
        'S': 'save_image',
        'X': 'exit'
    }

    def create(self, parameters):
        """
        Creates a new matrix containing only white pixels.
        :param parameters: x, y
        """
        self.elements = [self.WHITE_PIXEL * int(parameters[0]) for row in range(int(parameters[1]))]

    def clean(self):
        """
        Cleans matrix by switching all elements to white pixels.
        """
        m, n = self.length()
        self.create([m, n])

    def draw_element(self, parameters):
        """
        Colors element at position x, y.
        :param parameters: x, y, color
        """
        x = abs(int(parameters[0]))
        y = abs(int(parameters[1]))
        color = str(parameters[2]).upper()

        if 0 in (x, y):
            raise ValueError

        self.elements[y-1][x-1] = color

    def draw_column(self, parameters):
        """
        Colors column x from rows y1 to y2.
        :param parameters: x, y1, y2, color
        """
        for y in range(int(parameters[1]), int(parameters[2])+1):
            self.draw_element([int(parameters[0]), y, parameters[3]])

    def draw_row(self, parameters):
        """
        Colors row y from columns x1 to x2.
        :param parameters: x1, x2, y, color
        """
        for x in range(int(parameters[0]), int(parameters[1])+1):
            self.draw_element([x, int(parameters[2]), parameters[3]])

    def draw_rectangle(self, parameters):
        """
        Colors a rectangle.
        :param parameters: x1, y1, x2, y2, color
        """
        for y in range(int(parameters[1]), int(parameters[3])+1):
            self.draw_row([int(parameters[0]), int(parameters[2]), y, parameters[4]])

    def draw_area(self, parameters):
        """
        Colors an area.
        :param parameters: x, y, color
        """
        self.fill(int(parameters[0]) - 1, int(parameters[1]) - 1, parameters[2].upper())

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

    def save_image(self, parameters):
        """
        Saves an image into a file.
        :param parameters: name
        :return:
        """
        # Save to a file
        with open("images/{0}".format(parameters[0]), "w") as image_file:
            image_file.write(str(self.to_table(self.elements)))

        # Save to outputs
        self.outputs.append({"name": parameters[0], "matrix": self.elements})
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

        if command not in matrix.commands.keys():
            continue

        elif command == 'X':
            matrix.show()
            print("Program exited.")
            break

        getattr(matrix, matrix.commands[command])(parameters)

if __name__ == '__main__':
    main()
