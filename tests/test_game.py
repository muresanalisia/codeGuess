import unittest

from game.game import Game


class TestGame(unittest.TestCase):

    def test_digits1(self):
        game = Game()
        digits=game.digits(number=1267)
        print(digits)
        assert(len(digits)==4)
        assert(digits[0]==1)
        assert(digits[1]==2)
        assert(digits[2]==6)
        assert(digits[3]==7)

    def test_valid_code(self):
        game = Game()
        result=game.validate_code(number=8087)
        print(result)
        assert(result==True)