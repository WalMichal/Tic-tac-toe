from unittest import TestCase
from Model import GameModel

class TestGameModel(TestCase):
    def test_getResult(self):
        m = GameModel.GameModel()
        m.insert_sign((0,0))
        m.insert_sign((1,0))
        m.insert_sign((0,1))
        m.insert_sign((1,1))
        m.insert_sign((0,2))

        assert m.get_result()==1
        m.init()

        m.insert_sign((0,0))
        m.insert_sign((1,0))
        m.insert_sign((0,1))
        m.insert_sign((1,1))
        m.insert_sign((2,2))
        m.insert_sign((1,2))

        m.init()
        assert m.get_result() == 0

        m.init()
        m.insert_sign((0,0))
        m.insert_sign((1,0))
        m.insert_sign((2,0))
        m.insert_sign((0,2))
        m.insert_sign((1,2))
        m.insert_sign((2,2))
        m.insert_sign((0,1))
        m.insert_sign((1,1))
        m.insert_sign((2,1))

        assert m.get_result() == 3

