class Survivor:

    def __init__(self, name):
        self._name = name
        self._wounds = 0
        self._is_dead = False
        self._actions = 3
        self._equipments = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def wounds(self):
        return self._wounds

    @wounds.setter
    def wounds(self, new_wounds):
        self._wounds = new_wounds
        if self._wounds >= 2:

            self._is_dead = True
        else:
            self._is_dead = False 

    @property
    def is_dead(self):
        return self._is_dead

    @property
    def actions(self):
        return self._actions

    @property
    def equipments(self):
        return self._equipments

    def pick_equipment(self, equipment):
        if len(self._equipments) < 5:
            self._equipments.append(equipment)
        else:
            raise Exception("Cannot pick more than five pieces of equipment")
 