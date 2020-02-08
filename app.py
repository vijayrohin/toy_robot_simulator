# Main Program
"""
DESCRIPTION: * To import toy_robot for creating the class object of ToyRobot.
             * To get input from users using commmandline.
             * To verify each input entered by user using macros for valid commands
             * To result the output to the user via report function from ToyRobot Class.
"""

from toy_robot import ToyRobot
from macros import TOY_ROBOT_DIRECTIONS, TOY_TURN_POSITIONS, TOY_MAIN_COMMANDS
import re

# To check if any space present, to consider it as PLACE command
# Returns True/False based on space present in string
def check_space_present( given_string ):
	result_val = False
	if given_string.count(' ') == 1 and (given_string.split(" ")[0]).upper() == TOY_MAIN_COMMANDS[0] and given_string.count(',') == 2: # Condition to check if number of spaces present is 1 and Given command is PLACE and string content has 2 commas
		result_val = True
	elif (given_string.split(" ")[0]).upper() == TOY_MAIN_COMMANDS[0] and given_string.count(',') == 2: # Condition to check if given command is PLACE and string content has 2 commas
		result_val = True
	return result_val

# To parse PLACE command and segregate parameters for forwarding it to ToyRobot class
# Returns parsed parameters along with PLACE command or null
def parse_place_command( forwarded_string ):
	parsed_content = forwarded_string.split(" ", 1) # Getting the command alone seperate (PLACE)
	parsed_content_cmd = parsed_content[0] # Assignment of command chosen
	parsed_content_parameters = parsed_content[1] # Assignment of parameters provided along with command
	parsed_content_parameters = parsed_content_parameters.replace(" ", "") # Replace extra spaces with none
	parsed_parameter_content = parsed_content_parameters.split(",") # Parsing the parameters using commas as delimiter
	# To check if parameters length is 3 and first two position parameters are numbers and last parameter is direction (NORTH, SOUTH, EAST, WEST)
	if len(parsed_parameter_content) != 3 or not (parsed_parameter_content[0]).replace(".","").strip().isdigit() or not (parsed_parameter_content[1]).replace(".","").strip().isdigit() or ((parsed_parameter_content[2]).strip().upper() not in TOY_ROBOT_DIRECTIONS):
		return None
	# Resultant dict construction
	parsed_dict = {
		"x_pos" : int(float((parsed_parameter_content[0]).strip())),
		"y_pos" : int(float((parsed_parameter_content[1]).strip())),
		"direction" : (parsed_parameter_content[2]).strip().upper()
	}
	return parsed_dict


# Main function for executing the functionality of the simulator
def execute_main():
	# install_all_packages(["readchar"])
	toy_robot_obj = ToyRobot()
	is_simulator_running = True
	print("-------------------------------------------------------------------------------")
	print("-------------------------Toy Robot Simulator ( 5 X 5 )-------------------------")
	print("-------------------------------------------------------------------------------")
	print("=========================Available Commands and Syntax=========================")
	print("-------------------------------------------------------------------------------")
	print("(1) PLACE [x_position],[y_position],[face_direction] - To place it on the table")
	print("*Parameters definitions:*")
	print("**[x_position] -> between 0 and 4")
	print("**[y_position] -> between 0 and 4")
	print("**[face_direction] -> NORTH,SOUTH,EAST,WEST")
	print("(2) MOVE - To move robot one step forward in its facing direction")
	print("(3) RIGHT - To turn robot 90 degrees to its right side")
	print("(4) LEFT - To turn robot 90 degrees to its left side")
	print("(5) REPORT - To print current positions and facing direction")
	print("(6) EXIT - To exit the simulator")
	print("===============================================================================")
	print("Type the input commands for the robot...")
	while is_simulator_running: # Infinte loop - stops only when user types in EXIT Command
		given_command = input("New Command: ") # Getting input from the user, single command at one instance
		orig_command = given_command
		ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])') # Removing any escape sequence characters included in raw string
		given_command = ansi_escape.sub('', given_command)
		given_command = given_command.strip()
		given_command_split_up = given_command.split(" ") # Splitting up to get the intended command
		invoked_command = (given_command_split_up[0]).upper()
		if invoked_command == "EXIT" and len(given_command_split_up) == 1: # To check if its exit command
			is_simulator_running = False
			print("Thanks for playing toy robot simulator!!!")
		elif invoked_command == TOY_MAIN_COMMANDS[0] and check_space_present( given_command ) and parse_place_command( given_command ) is not None: # To check if its PLACE command
			parsed_dict = parse_place_command( given_command ) # Parsing parameters 
			is_placement_valid = toy_robot_obj.validate_place_command( parsed_dict["x_pos"], parsed_dict["y_pos"], parsed_dict["direction"] ) # Validating parameter values for PLACE command
			if is_placement_valid: # if valid perform assignment for placing toy robot on the table
				toy_robot_obj.set_placement_position( parsed_dict["x_pos"], parsed_dict["y_pos"], parsed_dict["direction"] )
			else:
				print("Warning: Place command not recognized. Please enter a valid Place command (Refer from list above)")
		elif invoked_command == TOY_MAIN_COMMANDS[1] and len(given_command_split_up) == 1: # To check if its MOVE command
			return_val, comment = toy_robot_obj.move_forward()
			if not return_val:
				print(comment)
		elif invoked_command == TOY_MAIN_COMMANDS[2] and len(given_command_split_up) == 1: # To check if its REPORT command
			result = toy_robot_obj.report_overall_position()
			if result != "":
				print( result )
			else:
				print( "Warning: Toy Robot is not placed on the table. Please use a valid Place command to place it on table." )
		elif invoked_command == TOY_MAIN_COMMANDS[3] and len(given_command_split_up) == 1: # To check if its LEFT command
			return_val, comment = toy_robot_obj.turn_position(invoked_command)
			if not return_val:
				print(comment)
		elif invoked_command == TOY_MAIN_COMMANDS[4] and len(given_command_split_up) == 1: # To check if its RIGHT command
			return_val, comment = toy_robot_obj.turn_position(invoked_command)
			if not return_val:
				print(comment)
		else:
			if 'x' in repr(orig_command):
				print("Warning: Command not recognized. Please enter a valid command (Refer from list above)")
			else:
				print("Warning: Command not recognized. Please enter a valid command (Refer from list above)")

if __name__ == '__main__':
	execute_main()

#EOF