from main.game import Game


class TestGameHistory:

    def test_game_history_begins_by_recording_time(self):
        game = Game()
        assert len(game.history) == 1
        first_game_event = game.history[0]
        assert first_game_event.action == "started game"
        assert first_game_event.timestamp != None
