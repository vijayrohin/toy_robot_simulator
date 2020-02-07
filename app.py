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
# Returns True/False based on space present in string
def check_space_present( given_string ):
	pass

# To parse PLACE command and segregate parameters for forwarding it to ToyRobot class
# Returns parsed parameters along with PLACE command or null
def parse_place_command( forwarded_string ):
	pass

# Main function for executing the functionality of the simulator
def execute_main():
	toy_robot_obj = ToyRobot()
	is_simulator_running = True
	print("-----------------------------------------------------------------------------------------")
	print("--------------------------------Play with Toy Robot ( 5 X 5 )----------------------------")
	print("-----------------------------------------------------------------------------------------")
	print("Type the input commands for the robot:")
	while is_simulator_running: # Infinte loop - stops only when user types in EXIT Command
		given_command = input("CMD:") # Getting input from the user, single command at one instance
		given_command_split_up = given_command.split(" ")
		invoked_command = (given_command_split_up[0]).upper()
		if invoked_command == "EXIT" and len(given_command_split_up) == 1: # To check if its exit command
			is_simulator_running = True
		elif invoked_command == TOY_MAIN_COMMANDS[0] and check_space_present( given_command ) and parse_place_command( given_command ) is not None: # To check if its PLACE command
			pass
		elif invoked_command == TOY_MAIN_COMMANDS[1] and len(given_command_split_up) == 1: # To check if its MOVE command
			pass
		elif invoked_command == TOY_MAIN_COMMANDS[2] and len(given_command_split_up) == 1: # To check if its REPORT command
			pass
		elif invoked_command == TOY_MAIN_COMMANDS[3] and len(given_command_split_up) == 1: # To check if its LEFT command
			pass
		elif invoked_command == TOY_MAIN_COMMANDS[4] and len(given_command_split_up) == 1: # To check if its RIGHT command
			pass

if __name__ == '__main__':
	execute_main()