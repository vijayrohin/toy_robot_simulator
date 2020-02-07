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
	if len(parsed_content_parameters) != 3 or not parsed_parameter_content[0].isdigit() or not parsed_parameter_content[1].isdigit() or (parsed_parameter_content[2].upper() not in TOY_ROBOT_DIRECTIONS):
		return None
	# Resultant dict construction
	parsed_dict = {
		"x_pos" = int(float(parsed_parameter_content[0])),
		"y_pos" = int(float(parsed_parameter_content[1])),
		"direction" = parsed_parameter_content[2].upper()
	}
	return parsed_dict


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
			parsed_dict = parse_place_command( given_command ) # Parsing parameters 
			is_placement_valid = toy_robot_obj.validate_place_command( parsed_dict.x_pos, parsed_dict.y_pos, parsed_dict.direction ) # Validating parameter values for PLACE command
			if( is_placement_valid ) { # if valid perform assignment for placing toy robot on the table
				toy_robot_obj.set_placement_position( parsed_dict.x_pos, parsed_dict.y_pos, parsed_dict.direction )
			}
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