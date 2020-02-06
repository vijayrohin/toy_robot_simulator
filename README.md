# Repository for developing a simulator for Toy Robot

#### Sketches of important points of simulator

##### Directions:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; North\
West <--|-->East\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; South

##### Table Structure:
-----------------------------
 0,4 | 1,4 | 2,4 | 3,4 | 4,4 
-----------------------------
 0,3 | 1,3 | 2,3 | 3,3 | 4,3 
-----------------------------
 0,2 | 1,2 | 2,2 | 3,2 | 4,2 
-----------------------------
 0,1 | 1,1 | 2,1 | 3,1 | 4,1 
-----------------------------
 0,0 | 1,0 | 2,0 | 3,0 | 4,0 
-----------------------------

##### Available commands: PLACE, MOVE, LEFT, RIGHT, REPORT
where PLACE command has three parameters x_position, y_position and Direction (NORTH, SOUTH, EAST, WEST)

Available commands are stored as macros in seperate file for easy accessibility.

#### Proposed Solution:
1) To create a class for ToyRobot for its placement, movements and position changes on the table.
2) Main function performs the functionality of getting input from the user and its validation using other sub functions.

#### Testcases:
1) Unit test to be carried out using unittest package in python.
2) Ad-hoc testcases for integration testing are also included in Testcases folder.
