import unittest
from toy_robot import ToyRobot

class ToyRobotTestCases(unittest.TestCase):

    def test_validate_place_command(self):
        toy_robot_obj = ToyRobot()
        self.assertEqual(toy_robot_obj.validate_place_command(0,1,"NORTH"), True)
        self.assertEqual(toy_robot_obj.validate_place_command(0,1,"North"), True)
        self.assertEqual(toy_robot_obj.validate_place_command('0','1',"NORTH"), True)
        self.assertEqual(toy_robot_obj.validate_place_command(5,1,"NORTH"), False)
        self.assertEqual(toy_robot_obj.validate_place_command(0,1,"SOUTH-WEST"), False)
        self.assertEqual(toy_robot_obj.validate_place_command('5','1',"NORTH"), False)

if __name__ == '__main__':
    unittest.main()