class Survivor:

    def __init__(self, name):
        self._name = name
        self._wounds = 0
        self._is_dead = False
        self._actions_remaining = 3
        self._in_hand_equipment = []
        self._in_reserve_equipment = []
        self._max_capacity = 5


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
        if self._wounds == 1 and len(self._in_hand_equipment + self._in_reserve_equipment) == 5:
            self._in_reserve_equipment.pop()
        if self._wounds == 1:
            self._max_capacity = 4
        if self._wounds >= 2:

            self._is_dead = True
        else:
            self._is_dead = False

    @property
    def is_dead(self):
        return self._is_dead

    @property
    def actions_remaining(self):
        return self._actions_remaining

    @property
    def in_hand_equipment(self):
        return self._in_hand_equipment

    @property
    def in_reserve(self):
        return self._in_reserve_equipment

    @property
    def max_capacity(self):
        return self._max_capacity

    def pick_equipment(self, equipment):
        if len(self._in_hand_equipment + self._in_reserve_equipment) < self._max_capacity:
            if len(self._in_hand_equipment) < 2:
                self._in_hand_equipment.append(equipment)
            else:
                if len(self._in_reserve_equipment) < 3:
                    self._in_reserve_equipment.append(equipment)
        else:
            raise Exception("Limit reached")

 #Wounds function, how to Coll into a collection for something, remove the equipment array
#Test cases: no reserve equipment and 1 wound, no equipment and 1 wound



