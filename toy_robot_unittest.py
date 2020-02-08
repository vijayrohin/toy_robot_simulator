# Unittest cases for each functionality

import unittest
from toy_robot import ToyRobot
from app import *

class ToyRobotTestCases(unittest.TestCase):

    # Test function for validating place command
    def test_validate_place_command(self):
        toy_robot_obj = ToyRobot()
        self.assertEqual(toy_robot_obj.validate_place_command(0,1,"NORTH"), True)
        self.assertEqual(toy_robot_obj.validate_place_command(0,1,"North"), True)
        self.assertEqual(toy_robot_obj.validate_place_command(0,1,"NOTH"), False)
        self.assertEqual(toy_robot_obj.validate_place_command(5,1,"NORTH"), False)
        self.assertEqual(toy_robot_obj.validate_place_command(0,1,"SOUTH-WEST"), False)
        self.assertEqual(toy_robot_obj.validate_place_command(5,1,"NORTH"), False)

    # Test function for validating move command
    def test_move_forward_command(self):
        toy_robot_obj = ToyRobot()
        toy_robot_obj.set_placement_position(0,1,"EAST")
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], False)
        self.assertEqual((toy_robot_obj.move_forward())[0], False)

    # Test function for validating turn command
    def test_turn_position(self):
        toy_robot_obj = ToyRobot()
        toy_robot_obj.set_placement_position(0,1,"EAST")
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        toy_robot_obj.turn_position("LEFT")
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], False)

    # Test function for validating report command
    def test_report_overall_position(self):
        toy_robot_obj = ToyRobot()
        toy_robot_obj.set_placement_position(0,0,"NORTH")
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        toy_robot_obj.turn_position("RIGHT")
        toy_robot_obj.turn_position("LEFT")
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        toy_robot_obj.turn_position("RIGHT")
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        toy_robot_obj.turn_position("RIGHT")
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], True)
        self.assertEqual((toy_robot_obj.move_forward())[0], False)
        self.assertEqual(toy_robot_obj.report_overall_position(), "2,0,SOUTH")

    # Test function for validating place command's space availability
    def test_check_space_present(self):
        self.assertEqual(check_space_present("PLACE 0,0,NORTH"), True)
        self.assertEqual(check_space_present("PLACE 0,0, NORTH"), True)
        self.assertEqual(check_space_present("PL ACE 0,0,NORTH"), False)
        self.assertEqual(check_space_present("Place 0,0, No rth"), True)

    # Test function for parsing place command
    def parse_place_command(self):
        parsed_val = {"x_pos": 0, "y_pos": 0, "direction": "NORTH"}
        self.assertEqual(parse_place_command("PLACE 0,0,NORTH"), parsed_val)
        parsed_val = {"x_pos": 1, "y_pos": 0, "direction": "South"}
        self.assertEqual(parse_place_command("Place 1,0,South"), parsed_val)
        parsed_val = None
        self.assertEqual(parse_place_command("PLACE 5,0,NORTH"), parsed_val)
        parsed_val = None
        self.assertEqual(parse_place_command("PLATE 1,0,NORTH"), parsed_val)

if __name__ == '__main__':
    unittest.main()