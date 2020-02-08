# Toy Robot Class file

"""
DESCRIPTION: * To create the toy_robot with its properties.
             * To assign the properties like x_position, y_position and facing_direction for toy_robot.
             * To check and verify the values of properties whether they are valid or not.
"""

from macros import TOY_ROBOT_DIRECTIONS, TOY_TURN_POSITIONS, TOY_MAIN_COMMANDS, TOY_OPERATOR_CMD_DICT, TOY_TURN_POS_VAL
import operator

# Class for Toy-Robot creation and movements

class ToyRobot:
	# Initialization of class variables (Constructor)
	def __init__(self):
		self._x_pos = -1
		self._y_pos = -1
		self._face_dir = ""
		self.dir_operators = { "+": operator.add, "-": operator.sub }

	# Setting up the position of Toy Robot on the table (Class function/Member Function)
	# Returns null
	def set_placement_position(self, gvn_x_pos, gvn_y_pos, gvn_face_dir):
		self._x_pos = gvn_x_pos
		self._y_pos = gvn_y_pos
		self._face_dir = gvn_face_dir

	# Validation of Place Command read from the user (Class function/Member Function)
	# Returns True/False
	def validate_place_command(self, gvn_x_pos, gvn_y_pos, gvn_face_dir):
		is_param_valid = False
		if gvn_x_pos > -1 and gvn_x_pos < 5 and gvn_y_pos > -1 and gvn_y_pos < 5 and gvn_face_dir.upper() in TOY_ROBOT_DIRECTIONS:
			is_param_valid = True
		return is_param_valid

	# To check and move the Toy Robot in current direction by one unit place (Class function/Member Function)
	# Returns True/False
	def move_forward(self):
		is_move_cmd_valid = True
		comment = ""
		if self._x_pos > -1 and self._y_pos > -1: # To check if toy robot has been placed on the table already
			# To check if Toy Robot's direction is North and move forward along the column if toy robot doesn't fall off the table (Eg: Orig Place: (3,1) -> MOVE -> Moved Place: (3,2))
			if TOY_ROBOT_DIRECTIONS[0] == self._face_dir and self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[0]]](self._y_pos, 1) < 5: 
				self._y_pos = self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[0]]](self._y_pos, 1)
			# To check if Toy Robot's direction is South and move backward along the column if toy robot doesn't fall off the table (Eg: Orig Place: (3,1) -> MOVE -> Moved Place: (3,0))
			elif TOY_ROBOT_DIRECTIONS[1] == self._face_dir and self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[1]]](self._y_pos, 1) > -1:
				self._y_pos = self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[1]]](self._y_pos, 1)
			# To check if Toy Robot's direction is East and move forward along the row if toy robot doesn't fall off the table (Eg: Orig Place: (3,1) -> MOVE -> Moved Place: (4,1))
			elif TOY_ROBOT_DIRECTIONS[2] == self._face_dir and self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[2]]](self._x_pos, 1) < 5:
				self._x_pos = self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[2]]](self._x_pos, 1)
			# To check if Toy Robot's direction is West and move forward along the row if toy robot doesn't fall off the table (Eg: Orig Place: (3,1) -> MOVE -> Moved Place: (2,1))
			elif TOY_ROBOT_DIRECTIONS[3] == self._face_dir and self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[3]]](self._x_pos, 1) > -1:
				self._x_pos = self.dir_operators[TOY_OPERATOR_CMD_DICT[TOY_ROBOT_DIRECTIONS[3]]](self._x_pos, 1)
			else:
				is_move_cmd_valid = False
				comment = "Warning: Toy Robot cannot be moved forward, because it will fall off the table"
		else:
			is_move_cmd_valid = False
			comment = "Warning: Toy Robot is not placed on the table. Please use a valid Place command to first place it on table. Example: 'PLACE 0,0,NORTH'"
		return is_move_cmd_valid, comment

	# To turn the Toy Robot on either side left or right after verification (Class function/Member Function)
	# Returns True/False
	def turn_position(self, direction):
		is_turn_cmd_valid = False
		comment = ""
		if self._x_pos > -1 and self._y_pos > -1: # To check if toy robot has been placed on the table already
			available_directions = TOY_TURN_POS_VAL[self._face_dir]
			self._face_dir = available_directions[direction]
			is_turn_cmd_valid = True
		else:
			comment = "Warning: Toy Robot is not placed on the table. Please use a valid Place command to first place it on table. Example: 'PLACE 0,0,NORTH'"
		return is_turn_cmd_valid, comment

	# To report the position of the Toy Robot along with its facing direction (Class function/Member Function)
	# Returns the position and direction in form of a string
	def report_overall_position(self):
		resultant_val = ""
		if self._x_pos > -1 and self._y_pos > -1:
			resultant_val = resultant_val + str(self._x_pos) + "," + str(self._y_pos) + "," + self._face_dir
		return resultant_val
# EOF