import datetime

from main.game import Game
from main.survivor import Survivor
from main.enum import Equipment
from unittest.mock import MagicMock, patch

#future idea: mock datetime

class TestGameHistory:
    #@patch("datetime.datetime.now", return_value=MagicMock())
    def test_game_history_begins_by_recording_time(self):
        #mock_datetime_now.return_value = datetime(2001, 1, 1)
        #datetime_mock = MagicMock(wrap=datetime.datetime)
        #mock_datetime_now.return_value = datetime.datetime(2020, 3, 11, 0, 0, 0)
        #monkeypatch.setattr(datetime, "datetime", datetime_mock)
        game = Game()
        assert len(game.history) == 1
        first_game_event = game.history[0]
        assert first_game_event.action == "Started Game"
        assert first_game_event.timestamp is not None

    def test_game_history_survivor_added(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)
        assert len(game.history) == 2
        first_game_event = game.history[1]
        assert first_game_event.action == "Survivor Added"

    def test_game_history_survivor_picks_equipment(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)
        game.survivor_picks_equipment(survivor, Equipment.KATANA)

        assert len(game.history) == 3
        equipment_obtained_game_event = game.history[2]
        assert equipment_obtained_game_event.action == "Survivor Picked Up Equipment"

    def test_game_history_survivor_gets_wound(self):
        game = Game()
        survivor = Survivor("Becky")
        game.add_survivor(survivor)
        game.survivor_gets_an_ouch(survivor)

        assert len(game.history) == 3
        survivor_gets_an_ouch_game_event = game.history[2]
        assert survivor_gets_an_ouch_game_event.action == "Survivor Is Wounded"
