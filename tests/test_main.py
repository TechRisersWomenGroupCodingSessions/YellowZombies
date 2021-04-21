# write tests here, don't forget to import what you need and
# info: https://docs.pytest.org/en/latest/getting-started.html#group-multiple-tests-in-a-class
from main.main import Survivor


class TestZombies:

    def test_check_survivor_has_name(self):
        survivor=Survivor()
        
        assert survivor.name== "Judy" 

    def test_check_survivor_has_zero_wounds(self):
        survivor=Survivor()
        
        assert survivor.wounds== 0

    # def test_died_after_two_wounds(self):
    #     survivor1=Survivor()
    #     survivor2=Survivor()
    #     survivor1.wounds=2
    #     survivor1.wounds=1
    #     assert survivor1.dead== True
    #     assert survivor2.dead== False