#rename test to whatever random name aishah comes up with that day

from main.game import Game


class TestGame:

    def test_game_begins_with_zero_survivors(self):
        game = Game()
        assert game.survivors_remaining() == 0




