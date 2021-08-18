from main.game import Game


class TestGamingHistory:

    def test_game_history_begins_by_recording_time(self):
        game = Game()
        assert len(game.history) > 0
