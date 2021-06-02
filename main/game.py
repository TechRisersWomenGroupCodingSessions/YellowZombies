#rename game to whatever random name aishah comes up with that day
from main.survivor import Survivor


class Game:

    def __init__(self):
        self._survivors = []

    @property
    def survivors(self):
        return self._survivors

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
