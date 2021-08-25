from main.game import Game
from main.survivor import Survivor


class TestGameHistory:

    def test_game_history_begins_by_recording_time(self):
        game = Game()
        assert len(game.history) == 1
        first_game_event = game.history[0]
        assert first_game_event.action == "started game"
        assert first_game_event.timestamp != None

    def test_game_history_survior_added(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)
        assert len(game.history) == 2
        first_game_event = game.history[1]
        assert first_game_event.action == "Survivor Added"
