# Repository for developing a simulator for Toy Robot

#### Sketches of important points of simulator

##### Directions:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; North\
West <--|-->East\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; South

##### Table Structure:
<table>
  <tr>
    <td>0,4</td>
    <td>1,4</td>
    <td>2,4</td>
    <td>3,4</td>
    <td>4,4</td>
  </tr>
  <tr>
    <td>0,3</td>
    <td>1,3</td>
    <td>2,3</td>
    <td>3,3</td>
    <td>4,3</td>
  </tr>
  <tr>
    <td>0,2</td>
    <td>1,2</td>
    <td>2,2</td>
    <td>3,2</td>
    <td>4,2</td>
  </tr>
   <tr>
    <td>0,1</td>
    <td>1,1</td>
    <td>2,1</td>
    <td>3,1</td>
    <td>4,1</td>
  </tr>
   <tr>
    <td>0,0</td>
    <td>1,0</td>
    <td>2,0</td>
    <td>3,0</td>
    <td>4,0</td>
  </tr>
</table>

##### Available commands: PLACE, MOVE, LEFT, RIGHT, REPORT
where PLACE command has three parameters x_position, y_position and Direction (NORTH, SOUTH, EAST, WEST)

Available commands are stored as macros in seperate file for easy accessibility.

#### Proposed Solution:
1) To create a class for ToyRobot for its placement, movements and position changes on the table.
2) Main function performs the functionality of getting input from the user and its validation using other sub functions.

#### Testcases:
1) Unit test to be carried out using unittest package in python.
2) Ad-hoc testcases for integration testing are also included in Testcases folder.
