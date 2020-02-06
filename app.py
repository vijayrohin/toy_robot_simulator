# Main Program
"""
DESCRIPTION: * To import toy_robot for creating the class object of ToyRobot.
             * To get input from users using commmandline.
             * To verify each input entered by user using macros for valid commands
             * To result the output to the user via report function from ToyRobot Class.
"""

from toy_robot import ToyRobot
from macros import TOY_ROBOT_DIRECTIONS, TOY_TURN_POSITIONS, TOY_MAIN_COMMANDS

# To check if any space present, to consider it as PLACE command
def check_space_present( given_string ):
	pass

# To parse PLACE command and segregate parameters for forwarding it to ToyRobot class
def parse_place_command( forwarded_string ):
	pass

# Main function for executing the functionality of the simulator
def execute_main():
	toy_robot_obj = ToyRobot()
	report_generated = False
	print("-----------------------------------------------------------------------------------------")
	print("--------------------------------Play with Toy Robot ( 5 X 5 )----------------------------")
	print("-----------------------------------------------------------------------------------------")
	print("Type the input commands for the robot:")
	while not report_generated:
		given_command = input("CMD:")
		if given_command == "REPORT":
			report_generated = True

if __name__ == '__main__':
	execute_main()