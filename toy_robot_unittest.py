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

    def test_move_forward_command(self):
        toy_robot_obj = ToyRobot()
        toy_robot_obj.set_placement_position(0,1,"EAST")
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), False)
        self.assertEqual(toy_robot_obj.move_forward(), False)

    def test_turn_position(self):
        toy_robot_obj = ToyRobot()
        toy_robot_obj.set_placement_position(0,1,"EAST")
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), True)
        toy_robot_obj.turn_position("LEFT")
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), False)

    def test_report_overall_position(self):
        toy_robot_obj = ToyRobot()
        toy_robot_obj.set_placement_position(0,0,"NORTH")
        self.assertEqual(toy_robot_obj.move_forward(), True)
        toy_robot_obj.turn_position("RIGHT")
        toy_robot_obj.turn_position("LEFT")
        self.assertEqual(toy_robot_obj.move_forward(), True)
        toy_robot_obj.turn_position("RIGHT")
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), True)
        toy_robot_obj.turn_position("RIGHT")
        self.assertEqual(toy_robot_obj.move_forward(), True)
        self.assertEqual(toy_robot_obj.move_forward(), False)
        self.assertEqual(toy_robot_obj.report_overall_position(), "4,1,EAST")

if __name__ == '__main__':
    unittest.main()