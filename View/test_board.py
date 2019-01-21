from unittest import TestCase
from View import Board as b
import os.path
class TestBoard(TestCase):
    def test_getFieldCoordinates(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path = os.path.normpath(my_path).replace('\\', '/').replace("Controller", "View")
        board = b.Board([[0,0,0],[0,0,0],[0,0,0]],my_path + '/board-texture.png',(150,200))

        self.event_coord = (150,200)
        self.result = board.getFieldCoordinates(self.event_coord)
        assert self.result == (-1,-1)

        self.event_coord = (180,220)
        self.result = board.getFieldCoordinates(self.event_coord)
        assert self.result == (0,0)

        self.event_coord = (300,350)
        self.result = board.getFieldCoordinates(self.event_coord)
        assert self.result == (1,1)