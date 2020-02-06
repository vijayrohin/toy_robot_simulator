# Toy Robot Class file

"""
DESCRIPTION: * To create the toy_robot with its properties.
             * To assign the properties like x_position, y_position and facing_direction for toy_robot.
             * To check and verify the values of properties whether they are valid or not.
"""

# Class for Toy-Robot creation and movements

class ToyRobot:
	# Initialization of class variables (Constructor)
	def __init__(self):
		self.x_pos = -1
		self.y_pos = -1
		self.face_dir = ""

	# Setting up the position of Toy Robot on the table (Class function/Member Function)
	# Returns null
	def set_placement_position(self, gvn_x_pos, gvn_y_pos, gvn_face_dir):
		pass

	# Validation of Place Command read from the user (Class function/Member Function)
	# Returns True/False
	def validate_place_command(self, gvn_x_pos, gvn_y_pos, gvn_face_dir):
		pass

	# To check and move the Toy Robot in current direction by one unit place (Class function/Member Function)
	# Returns True/False
	def move_forward(self):
		pass

	# To turn the Toy Robot on either side left or right after verification (Class function/Member Function)
	# Returns True/False
	def turn_position(self, direction):
		pass

	# To report the position of the Toy Robot along with its facing direction (Class function/Member Function)
	# Returns the position and direction in form of a string
	def report_overall_position(self):
		pass

# EOF