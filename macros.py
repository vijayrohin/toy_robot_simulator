# Macros for Toy Robot Application

# Toy Robot Available Directions
TOY_ROBOT_DIRECTIONS = ["NORTH","SOUTH","EAST","WEST"]

# Toy Robot Available Turn Positions
TOY_TURN_POSITIONS = ["LEFT","RIGHT"]

# Toy Robot Available Main Commands
TOY_MAIN_COMMANDS = ["PLACE","MOVE","REPORT","LEFT","RIGHT"]

# Toy Robot Operator Functionality
TOY_OPERATOR_CMD_DICT = { "NORTH": "+", "SOUTH": "-", "EAST": "+", "WEST": "-" }

# Toy Robot Turn Positions and its values
TOY_TURN_POS_VAL = {
	"NORTH": { "LEFT": "WEST", "RIGHT": "EAST" },
	"SOUTH": { "LEFT": "EAST", "RIGHT": "WEST" },
	"EAST": { "LEFT": "NORTH", "RIGHT": "SOUTH" },
	"WEST": { "LEFT": "SOUTH", "RIGHT": "NORTH" }
}