#rename game to whatever random name aishah comes up with that day
from main.survivor import Survivor


class Game:

    def __init__(self):
        self._survivors = []
        self._level = "Blue"
        #self._game_over = False

    @property
    def survivors(self):
        return self._survivors

    @property
    def level(self):
        return self._level

    #@property
    #def game_over(self):
        #return self._game_over

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

        # survivors_name = [sur.name for sur in self.survivors]
        # for sur in self.survivors:
        #     if sur.name == survivor.name:
        #         raise Exception("Name already used")
        # self.survivors.append(survivor)

  