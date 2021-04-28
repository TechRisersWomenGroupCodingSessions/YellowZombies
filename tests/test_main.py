# write tests here, don't forget to import what you need and
# info: https://docs.pytest.org/en/latest/getting-started.html#group-multiple-tests-in-a-class
from main.main import Survivor


class TestZombies:

    def test_check_survivor_has_name(self):
        survivor = Survivor("Judy")
        
        assert survivor.name == "Judy" 

    def test_check_survivor_has_zero_wounds(self):
        survivor = Survivor("Judy")
        
        assert survivor.wounds == 0

    def test_survivor_dies_immediately_after_two_wounds(self):
        survivor = Survivor("Judy")

        survivor.wounds = 1
        assert survivor.is_dead is False
        
        survivor.wounds = 2
        assert survivor.is_dead is True
        
        survivor.wounds = 3
        assert survivor.is_dead is True

    def test_name_can_be_anything(self):
        survivor = Survivor("Becky")
        assert survivor.name == "Becky"

    def test_survivor_starts_with_3_actions(self):
        survivor = Survivor("Becky")
        assert survivor.actions == 3 #changename?

    def test_survivor_can_carry_up_to_five_pieces_of_equipment(self):
        survivor = Survivor("Becky")

        survivor.equipment_count = 3
        assert survivor.equipment_count == 3

        survivor.equipment_count = 5
        assert survivor.equipment_count == 5
        print(survivor.equipment_count)
