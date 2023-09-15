import unittest
from spacecraft import * 

class Main(unittest.TestCase):

    def test1(self):
        chandrayaan = SpaceCraft()
        chandrayaan.move('f','N')
        self.assertEqual(chandrayaan.getPosition(), [0, 1, 0])

    def test2(self):
        chandrayaan = SpaceCraft()
        chandrayaan.move('b','N')
        self.assertEqual(chandrayaan.getPosition(), [0, -1, 0])

    def test3(self):
        chandrayaan = SpaceCraft()
        chandrayaan.turn('l','N')
        self.assertEqual(chandrayaan.getDirection(), 'W')

    def test4(self):
        chandrayaan = SpaceCraft()
        chandrayaan.turn('r','E')
        self.assertEqual(chandrayaan.getDirection(), 'S')

    def test5(self):
        chandrayaan = SpaceCraft()
        chandrayaan.tilt('u','N')
        self.assertEqual(chandrayaan.getDirection(), 'U')

    def test6(self):
        chandrayaan = SpaceCraft()
        chandrayaan.tilt('d','S')
        self.assertEqual(chandrayaan.getDirection(), 'D')

    def test7(self):
        chandrayaan = SpaceCraft()
        commands = ['f', 'r', 'u', 'b', 'l']
        chandrayaan.command_execute(commands)
        self.assertEqual(chandrayaan.getPosition(), [0, 1, -1])
        self.assertEqual(chandrayaan.getDirection(), 'N')

        commands=['b','l','u','r','f','f','l']
        chandrayaan.command_execute(commands)
        self.assertEqual(chandrayaan.getPosition(), [0, 2, -1])
        self.assertEqual(chandrayaan.getDirection(), 'W')

        commands=['f','f','u','u','l','l','b','b']
        chandrayaan.command_execute(commands)
        self.assertEqual(chandrayaan.getPosition(), [-4, 2, -1])
        self.assertEqual(chandrayaan.getDirection(), 'E')


       

