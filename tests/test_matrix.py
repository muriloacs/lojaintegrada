# -*- coding: utf8 -*-

import unittest
from app.matrix import Matrix


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.matrix = Matrix()
        
    def test_create(self):
        self.matrix.create(2, 2)
        self.assertEqual(self.matrix.elements[0][0], 0)
        self.assertEqual(self.matrix.elements[0][1], 0)
        self.assertEqual(self.matrix.elements[1][0], 0)
        self.assertEqual(self.matrix.elements[1][1], 0)

    def test_clean(self):
        self.matrix.create(2, 2)
        self.matrix.elements[0][0] = "A"
        self.matrix.elements[0][1] = "B"
        self.matrix.elements[1][0] = "C"
        self.matrix.elements[1][1] = "D"
        self.assertEqual(self.matrix.elements[0][0], "A")
        self.assertEqual(self.matrix.elements[0][1], "B")
        self.assertEqual(self.matrix.elements[1][0], "C")
        self.assertEqual(self.matrix.elements[1][1], "D")
        self.matrix.clean()
        self.assertEqual(self.matrix.elements[0][0], 0)
        self.assertEqual(self.matrix.elements[0][1], 0)
        self.assertEqual(self.matrix.elements[1][0], 0)
        self.assertEqual(self.matrix.elements[1][1], 0)

    def test_draw_element(self):
        self.matrix.create(2, 2)
        self.matrix.draw_element(1, 1, "A")
        self.assertEqual(self.matrix.elements[0][0], "A")
        self.assertEqual(self.matrix.elements[0][1], 0)
        self.assertEqual(self.matrix.elements[1][0], 0)
        self.assertEqual(self.matrix.elements[1][1], 0)

    def test_draw_column(self):
        self.matrix.create(3, 4)
        self.matrix.draw_column(2, 1, 3, "A")
        self.assertEqual(self.matrix.elements[0][0], 0)
        self.assertEqual(self.matrix.elements[0][1], "A")
        self.assertEqual(self.matrix.elements[0][2], 0)
        self.assertEqual(self.matrix.elements[1][0], 0)
        self.assertEqual(self.matrix.elements[1][1], "A")
        self.assertEqual(self.matrix.elements[1][2], 0)
        self.assertEqual(self.matrix.elements[2][0], 0)
        self.assertEqual(self.matrix.elements[2][1], "A")
        self.assertEqual(self.matrix.elements[2][2], 0)
        self.assertEqual(self.matrix.elements[3][0], 0)
        self.assertEqual(self.matrix.elements[3][1], 0)
        self.assertEqual(self.matrix.elements[3][2], 0)

    def test_draw_row(self):
        self.matrix.create(4, 3)
        self.matrix.draw_row(1, 3, 2, "A")
        self.assertEqual(self.matrix.elements[0][0], 0)
        self.assertEqual(self.matrix.elements[0][1], 0)
        self.assertEqual(self.matrix.elements[0][2], 0)
        self.assertEqual(self.matrix.elements[0][3], 0)
        self.assertEqual(self.matrix.elements[1][0], "A")
        self.assertEqual(self.matrix.elements[1][1], "A")
        self.assertEqual(self.matrix.elements[1][2], "A")
        self.assertEqual(self.matrix.elements[1][3], 0)
        self.assertEqual(self.matrix.elements[2][0], 0)
        self.assertEqual(self.matrix.elements[2][1], 0)
        self.assertEqual(self.matrix.elements[2][2], 0)
        self.assertEqual(self.matrix.elements[2][3], 0)

    def test_draw_rectangle(self):
        self.matrix.create(4, 3)
        self.matrix.draw_rectangle(2, 2, 4, 3, "A")
        self.assertEqual(self.matrix.elements[0][0], 0)
        self.assertEqual(self.matrix.elements[0][1], 0)
        self.assertEqual(self.matrix.elements[0][2], 0)
        self.assertEqual(self.matrix.elements[0][3], 0)
        self.assertEqual(self.matrix.elements[1][0], 0)
        self.assertEqual(self.matrix.elements[1][1], "A")
        self.assertEqual(self.matrix.elements[1][2], "A")
        self.assertEqual(self.matrix.elements[1][3], "A")
        self.assertEqual(self.matrix.elements[2][0], 0)
        self.assertEqual(self.matrix.elements[2][1], "A")
        self.assertEqual(self.matrix.elements[2][2], "A")
        self.assertEqual(self.matrix.elements[2][3], "A")

    def test_save_image(self):
        self.matrix.create(2, 2)
        self.matrix.draw_element(1, 1, "A")
        self.matrix.save_image('test_image')
        with open("images/test_image", "r") as image_file:
            image_content = image_file.read()
            self.assertIn("Field 1", image_content)
            self.assertIn("Field 2", image_content)
            self.assertIn("|    0    |", image_content)
            self.assertNotIn("|    1    |", image_content)

if __name__ == '__main__':
    unittest.main()
