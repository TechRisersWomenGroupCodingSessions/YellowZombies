#rename test to whatever random name aishah comes up with that day
from main.game import Game
from main.survivor import Survivor
from pytest import raises

class TestGame:

    def test_game_begins_with_zero_survivors(self):
        game = Game()
        assert game.survivors_remaining() == 0

    def test_game_add_a_survivor(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)

        assert game.survivors_remaining() == 1

    def test_survivor_is_unique(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)

        with raises(Exception) as unique_name_exception:
            game.add_survivor(survivor)

        assert "Name already used" in str(unique_name_exception.value)

    def test_survivor_name_is_unique(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)
        survivor2 = Survivor("Becky")

        with raises(Exception) as unique_name_exception:
            game.add_survivor(survivor2)

        assert "Name already used" in str(unique_name_exception.value)

    def test_survivor_name_is_not_unique(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)
        survivor2 = Survivor("Isabel")
        game.add_survivor(survivor2)

        assert game.survivors_remaining() == 2

    def test_game_ends_if_all_survivors_dead(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)
        survivor.ouch()
        survivor.ouch()

        assert game.game_status() is False



