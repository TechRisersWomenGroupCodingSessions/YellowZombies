#rename game to whatever random name aishah comes up with that day
from main.survivor import Survivor
from main.enum import Level
from operator import attrgetter
from main.game_event import GameEvent


class Game:

    def __init__(self):
        self._survivors = []
        self._history = [GameEvent("Started Game")]
        # self._level = Level.BLUE
        # self._game_over = False

    @property
    def survivors(self):
        return self._survivors

    @property
    def history(self):
        return self._history

    @property
    def level(self):
        if len(self.survivors) == 0:
            return Level.BLUE
        else:
            # survivors_experiences = list(map(lambda s: s.experience, self.survivors))
            # max_value = max(survivors_experiences)
            # max_index = survivors_experiences.index(max_value)
            highest_survivor = max(self.survivors, key=attrgetter("experience"))

            return highest_survivor.level

        # return self._level

    # @property
    # def game_over(self):
        # return self._game_over

# ahhhh think about this
    def game_status(self):
        survivors_alive = list(filter(lambda s: s.is_dead is False, self.survivors))
        if len(survivors_alive) == 0:
            return False
        else:
            return True

    def survivors_remaining(self):
        return len(self.survivors)

    def add_survivor(self, survivor):
        survivors_name = list(filter(lambda s: s.name == survivor.name, self.survivors))
        if len(survivors_name) > 0:
            raise Exception("Name already used")
        self.survivors.append(survivor)
        self._history.append(GameEvent("Survivor Added"))

        # survivors_name = [sur.name for sur in self.survivors]
        # for sur in self.survivors:
        #     if sur.name == survivor.name:
        #         raise Exception("Name already used")
        # self.survivors.append(survivor)

    def survivor_picks_equipment(self, survivor, equipment):
        survivor.pick_equipment(equipment)
        self._history.append(GameEvent("Survivor Picked Up Equipment"))
