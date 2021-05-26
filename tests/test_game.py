#rename test to whatever random name aishah comes up with that day
from main.game import Game
from main.survivor import Survivor


class TestGame:

    def test_game_begins_with_zero_survivors(self):
        game = Game()
        assert game.survivors_remaining() == 0

    def test_game_add_a_survivor(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)

        assert game.survivors_remaining() == 1
        assert survivor.name == "Becky"

